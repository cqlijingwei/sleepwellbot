from .base_agent import BaseAgent
import uuid

class OrdersAgent(BaseAgent):
    def process_query(self, query: str) -> str:
        if not self.is_enabled():
            return "Order service is currently unavailable."
        
        if 'place order' in query.lower():
            return self._place_order(query)
        
        if 'order status' in query.lower():
            return self._check_order_status(query)
        
        return "Could not process your order-related query."

    def _place_order(self, query: str) -> str:
        order_id = f'ORDER-{uuid.uuid4().hex[:8].upper()}'
        order_details = {
            'order_id': order_id,
            'customer_name': 'Customer',  # Extract from query
            'product_id': 'ultra_comfort',  # Extract from query
            'status': 'processing'
        }
        
        self.db.add_order(order_details)
        return json.dumps({
            'message': 'Order placed successfully',
            'order_id': order_id
        })

    def _check_order_status(self, query: str) -> str:
        # Extract order ID from query
        order_id = query.split()[-1]
        order = self.db.get_order(order_id)
        
        if order:
            return json.dumps({
                'order_id': order['order_id'],
                'status': order['status']
            })
        
        return "Order not found."