from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json
from config import Config
from database.database import DatabaseManager
from agents.product_details_agent import ProductDetailsAgent
from agents.product_reviews_agent import ProductReviewsAgent
from agents.orders_agent import OrdersAgent
from utils.conversation_router import ConversationRouter

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize database and agents
db_manager = DatabaseManager(Config.SQLITE_DB_PATH)
product_details_agent = ProductDetailsAgent(Config, db_manager)
product_reviews_agent = ProductReviewsAgent(Config, db_manager)
orders_agent = OrdersAgent(Config, db_manager)

conversation_router = ConversationRouter([
    product_details_agent, 
    product_reviews_agent, 
    orders_agent
])

@socketio.on('connect')
def handle_connect():
    emit('message', {
        'type': 'welcome',
        'message': 'Welcome to Sleep Better! I\'m Frodo, your personal sleep consultant.'
    })

@socketio.on('message')
def handle_message(data):
    query = data.get('message', '')
    try:
        response = conversation_router.route_query(query)
        emit('message', {
            'type': 'response',
            'message': response
        })
    except Exception as e:
        emit('message', {
            'type': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)