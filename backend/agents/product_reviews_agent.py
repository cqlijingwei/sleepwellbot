from .base_agent import BaseAgent
from typing import Dict
import json

class ProductReviewsAgent(BaseAgent):
    def __init__(self, config, db_manager):
        super().__init__(config, db_manager)
        self.reviews = {
            'ultra_comfort': [
                {"rating": 5, "text": "Best sleep ever!", "user": "John D."},
                # Add more reviews
            ],
            'dream_sleep': [
                {"rating": 4, "text": "Great for guest room", "user": "Maria C."},
                # Add more reviews
            ]
        }

    def process_query(self, query: str) -> str:
        if not self.is_enabled():
            return "Product reviews service is currently unavailable."
        
        # Logic to retrieve reviews
        for product, reviews in self.reviews.items():
            if product in query.lower():
                return json.dumps(reviews)
        
        return "No reviews found for the requested product."

    def add_review(self, product_id: str, review: Dict):
        if product_id not in self.reviews:
            return False
        self.reviews[product_id].append(review)
        return True