from .base_agent import BaseAgent
import json

class ProductDetailsAgent(BaseAgent):
    def process_query(self, query: str) -> str:
        if not self.is_enabled():
            return "Product details service is currently unavailable."
        
        # Implement product details logic
        products = {
            'ultra_comfort': self._get_ultra_comfort_details(),
            'dream_sleep': self._get_dream_sleep_details()
        }
        
        # Add logic to match query to product details
        for product_id, details in products.items():
            if product_id in query.lower():
                return json.dumps(details)
        
        return "Could not find product details for your query."

    def _get_ultra_comfort_details(self):
        return {
            "name": "Ultra Comfort Mattress",
            "price": "$1,299",
            "type": "Hybrid",
            "key_features": [
                "Cooling Gel Memory Foam",
                "Edge-to-edge support",
                "Motion isolation"
            ]
        }

    def _get_dream_sleep_details(self):
        return {
            "name": "Dream Sleep Mattress",
            "price": "$899",
            "type": "All-Foam",
            "key_features": [
                "Pressure-relieving memory foam",
                "Open-cell foam technology",
                "Zero motion transfer"
            ]
        }