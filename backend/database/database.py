import sqlite3
import json
from typing import Dict, List

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()
        self._load_initial_data()

    def _create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id TEXT PRIMARY KEY,
                    details TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT,
                    review TEXT,
                    rating INTEGER
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    order_id TEXT PRIMARY KEY,
                    customer_name TEXT,
                    product_id TEXT,
                    status TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def _load_initial_data(self):
        # Load product catalog from document
        products = [
            {"id": "ultra_comfort", "name": "Ultra Comfort Mattress", "details": "..."},
            {"id": "dream_sleep", "name": "Dream Sleep Mattress", "details": "..."},
            # Add other products from catalog
        ]
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for product in products:
                cursor.execute(
                    'INSERT OR REPLACE INTO products (id, details) VALUES (?, ?)', 
                    (product['id'], json.dumps(product))
                )
            conn.commit()

    def add_order(self, order_details: Dict):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO orders 
                (order_id, customer_name, product_id, status) 
                VALUES (?, ?, ?, ?)
            ''', (
                order_details['order_id'], 
                order_details['customer_name'], 
                order_details['product_id'], 
                'processing'
            ))
            conn.commit()

    def get_order(self, order_id: str) -> Dict:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
            return dict(cursor.fetchone()) if cursor.fetchone() else None
