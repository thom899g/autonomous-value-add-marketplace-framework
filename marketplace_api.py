"""
This module provides an API interface for interacting with the Marketplace Framework.
It enables external services and users to perform operations such as:
- Creating listings
- Buying assets
- Verifying assets
- Querying transaction history

The API is designed to be modular and scalable, supporting both RESTful HTTP requests
and WebSocket-based real-time updates.
"""

from flask import Flask, request, jsonify
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

marketplace_manager = MarketplaceManager()

@app.route('/create_listing', methods=['POST'])
def create_listing():
    """
    Creates a new asset listing on the marketplace.
    
    Request JSON:
        {
            "asset_id": "string",
            "owner_address": "string", 
            "price": number,
            "description": "string"
        }
        
    Returns:
        JSON with success status and error message if applicable
    """
    try:
        data = request.get_json()
        asset_id = data['asset_id']
        owner_address = data['owner_address']
        price = data['price']
        description = data['description']
        
        success = marketplace_manager.create_listing(
            asset_id, owner_address, price, description
        )
        
        return jsonify({'success