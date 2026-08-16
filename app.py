from flask import Flask, jsonify, request
from data import products
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return jsonify("Welcome to the Openfood Products API")

# 1. GET /inventory -> Fetch all items
@app.route('/inventory', methods=['GET'])
def get_all_inventory():
    return jsonify(products), 200

# 2. GET /inventory/<id> -> Fetch a single item 
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    found_item = None
    
    for item in products:
        if item.get('status') == item_id:
            found_item = item
            break  
            
    if found_item is not None:
        return jsonify(found_item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

# 3. POST /inventory -> Add a new item
@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    
    products.append(new_item)
    
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

# 4. PATCH /inventory/<id> -> Update an item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    found_item = None
    
    for item in products:
        if item.get('status') == item_id:
            found_item = item
            break
            
    if found_item is None:
        return jsonify({"error": "Item not found"}), 404
        
    update_data = request.get_json()
    found_item.update(update_data)
    
    return jsonify({"message": "Item updated successfully", "item": found_item}), 200

# 5. DELETE /inventory/<id> -> Remove an item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    found_item = None
    
    for item in products:
        if item.get('status') == item_id:
            found_item = item
            break
            
    if found_item is not None:
        products.remove(found_item)
        return jsonify({"message": f"The {item_id} was deleted successfully"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404



def fetch_from_openfoodfacts(query):
    headers = {'User-Agent': 'MyFlaskInventoryApp - LearningProject - Version 1.0'}
    
    if query.isdigit():
        url = f"https://world.openfoodfacts.org/api/v0/product/{query}.json"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == 1:
                return data.get("product")
    else:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            products_found = data.get("products", [])
            if len(products_found) > 0:
                return products_found[0]
                
    return None

# 6. GET /external/<query> -> Route endpoint
@app.route('/external/<string:query>', methods=['GET'])
def get_external_product(query):
    external_data = fetch_from_openfoodfacts(query)
    
    if external_data is not None:
        formatted_product = {
            "status": 1,
            "product": {
                "product_name": external_data.get("product_name", "Unknown Product"),
                "brands": external_data.get("brands", "Unknown Brand"),
                "ingredients_text": external_data.get("ingredients_text", "No ingredients listed")
            }
        }
        return jsonify(formatted_product), 200
    else:
        return jsonify({"error": "Product not found on OpenFoodFacts"}), 404



if __name__ == '__main__':
    app.run(debug=True)
