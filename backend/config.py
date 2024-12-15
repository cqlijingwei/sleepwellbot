import os

class Config:
    # Agent Configuration
    AGENTS = {
        'product_details': True,
        'product_reviews': True,
        'orders': True
    }

    # Database Configuration
    SQLITE_DB_PATH = os.path.join(os.path.dirname(__file__), 'sleep_better.db')
