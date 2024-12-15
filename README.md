# Sleep Better Support Chatbot

## Project Overview
Multi-agent customer support system for Sleep Better mattress company, featuring intelligent query routing and specialized backend agents.

## Prerequisites
- Python 3.8+
- pip

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/sleep-better-support.git
cd sleep-better-support
```
2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install dependencies

```bash
pip install -r requirements.txt
```
4. Run the application

```bash
uvicorn main:app --reload
```
Configuration

Edit config/config.yaml to modify agent settings and database configuration.

Testing

Comprehensive test suite coming soon!

Deployment Notes

# Sleep Better Support System

## Setup Instructions

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run the backend:
   python backend/app.py
5. Navigate to frontend directory
Run: npm install react-scripts --save-dev
Run: npm install
Run: HOST=localhost npm start

Use environment variables for sensitive configurations
Recommended to use a production WSGI server like Gunicorn

-- Backend with multiple specialized agents:

Product Details Agent
Product Reviews Agent
Orders Agent


-- Database integration with SQLite
-- Conversation routing mechanism
-- Configuration management
-- Frontend React application for chat interface

Key features:

Agents can be enabled/disabled via configuration
Intelligent query routing
Persistent order tracking
Scalable architecture

To run the project:

-- Set up backend:

Install requirements: pip install -r requirements.txt
Run backend: python backend/app.py


-- Set up frontend:

Navigate to frontend directory
Run: npm install react-scripts --save-dev
Run: npm install
Run: HOST=localhost npm start



The system demonstrates a multi-agent architecture with a unified frontend persona "Frodo" handling customer interactions across product details, reviews, and orders.