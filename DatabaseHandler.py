import sqlite3
from datetime import datetime
from collections import defaultdict
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DB_FILE = "finance_tracker.db"

# This list has each type of expense
DEFAULT_CATEGORIES = [ 
    "Rent",
    "Groceries",
    "Utilities",
    "Transport",
    "Dining",
    "Entertainment",
    "Health",
    "Subscriptions",
    "Shopping",
    "Other",
    "Savings",
]

# This class uses the sqlite3 library to let python make SQL commands and control a brand new database
class FinanceDB:
    def __init__(self, db_path=DB_FILE):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()
        self.seed_defaults()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0)
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS budget_allocations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                month_key TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0),
                UNIQUE(month_key, category)
            )
            """
        )
        self.conn.commit()

    # This method uses the list at the top to automatically place 
    # categories when the program is run
    def seed_defaults(self):
        cur = self.conn.cursor()
        for name in DEFAULT_CATEGORIES:
            cur.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)", (name,))
        defaults = {
            "monthly_income": "0",
            "custom_savings_percent": "20",
            "budget_method": "50/30/20 Rule",
        }
        for key, value in defaults.items():
            cur.execute(
                "INSERT OR IGNORE INTO settings(key, value) VALUES (?, ?)",
                (key, value),
            )
        self.conn.commit()

    def get_setting(self, key, default=""):
        row = self.conn.execute(
            "SELECT value FROM settings WHERE key = ?", (key,)
        ).fetchone()
        return row["value"] if row else default

    def set_setting(self, key, value):
        self.conn.execute(
            """
            INSERT INTO settings(key, value) VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
            """,
            (key, str(value)),
        )
        self.conn.commit()

    def get_categories(self):
        rows = self.conn.execute(
            "SELECT name FROM categories ORDER BY name COLLATE NOCASE"
        ).fetchall()
        return [row["name"] for row in rows]

    def add_category(self, name):
        self.conn.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)", (name,))
        self.conn.commit()

    # This method takes info from the BudgetTrackerApp class to put it in the database using SQL
    def add_transaction(self, date_text, trans_type, category, amount):
        self.conn.execute(
            "INSERT INTO transactions(date, type, category, amount) VALUES (?, ?, ?, ?)",
            (date_text, trans_type, category, amount),
        )
        self.conn.commit()

    def delete_transaction(self, tx_id):
        self.conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
        self.conn.commit()

    # This method specifies the transactions for the current month you have
    def get_transactions_for_month(self, month_key):
        rows = self.conn.execute(
            # substr(date, 1, 7) specifies to look for year and month
            """
            SELECT id, date, type, category, amount
            FROM transactions
            WHERE substr(date, 1, 7) = ?
            ORDER BY date DESC, id DESC
            """,
            (month_key,),
        ).fetchall()
        return rows

    def get_month_totals(self, month_key):
        rows = self.conn.execute(
            """
            SELECT type, COALESCE(SUM(amount), 0) AS total
            FROM transactions
            WHERE substr(date, 1, 7) = ?
            GROUP BY type
            """,
            (month_key,),
        ).fetchall()
        totals = {"Expense": 0.0, "Income": 0.0, "Savings": 0.0}
        for row in rows:
            totals[row["type"]] = float(row["total"])
        return totals

    def get_expense_totals_by_category(self, month_key):
        rows = self.conn.execute(
        """
        SELECT category, COALESCE(SUM(amount), 0) AS total
        FROM transactions
        WHERE substr(date, 1, 7) = ?
          AND type IN ('Expense', 'Savings')
        GROUP BY category
        ORDER BY total DESC, category
        """,
        (month_key,),
    ).fetchall()
        return {row["category"]: float(row["total"]) for row in rows}

    def save_allocations(self, month_key, allocations):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM budget_allocations WHERE month_key = ?", (month_key,))
        for category, amount in allocations.items():
            if amount > 0:
                cur.execute(
                    "INSERT INTO budget_allocations(month_key, category, amount) VALUES (?, ?, ?)",
                    (month_key, category, amount),
                )
        self.conn.commit()

    def get_allocations(self, month_key):
        rows = self.conn.execute(
            """
            SELECT category, amount
            FROM budget_allocations
            WHERE month_key = ?
            ORDER BY amount DESC, category
            """,
            (month_key,),
        ).fetchall()
        return {row["category"]: float(row["amount"]) for row in rows}


