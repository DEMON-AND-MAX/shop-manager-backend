from firebase_handler import FirebaseHandler
from flask import Flask, request, jsonify
from flask_cors import CORS

APP_NAME = "Shop Manager Backend"
APP_DEV = "Amalia Matioc, Maximilian Todea, Ariana Radu"

app = Flask(__name__)
CORS(app)

firebase_handler = FirebaseHandler()

### TESTING ROUTES
@app.route('/', methods=['GET'])
def app_base():
    return "Hello world! " + APP_NAME

@app.route('/get', methods=['GET'])
def app_get():
    response = jsonify({
        "message": "Response from " + APP_NAME + " by " + APP_DEV + "."
        })
    return response

@app.route('/post', methods=['POST'])
def app_post():
    data = request.get_json()
    print(data)
    response = jsonify({
        "message": "Response from " + APP_NAME + " by " + APP_DEV + ".",
        "data": data,
    })
    return response

### FIREBASE ROUTES
@app.route('/add-item', methods=['POST'])
def app_add_item():
    data = request.json

    required_fields = ["collection", "item_id", "data",]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    collection = data["collection"]
    item_id = data["item_id"]
    item_data = data["data"]

    firebase_handler.add_item(
        collection=collection,
        item_id=item_id,
        data=item_data,
    )

    return jsonify({"message": f"Added {item_id} to {collection}"}), 200

@app.route('/update-item', methods=['POST'])
def app_update_item():
    data = request.json

    required_fields = ["collection", "item_id", "updates",]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400
    
    collection = data["collection"]
    item_id = data["item_id"]
    updates = data["updates"]

    firebase_handler.update_item(
        collection=collection,
        item_id=item_id,
        updates=updates,
    )

    return jsonify({"message": f"Updated {item_id} in {collection}"}), 200

@app.route('/delete-item', methods=['POST'])
def app_delete_item():
    data = request.json

    required_fields = ["collection", "item_id",]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400
    
    collection = data["collection"]
    item_id = data["item_id"]

    firebase_handler.delete_item(
        collection=collection,
        item_id=item_id,
    )

    return jsonify({"message": f"Deleted {item_id} in {collection}"}), 200

@app.route('/get-item', methods=['POST'])
def app_get_item():
    data = request.json

    required_fields = ["collection", "item_id",]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400
    
    collection = data["collection"]
    item_id = data["item_id"]

    item_data = firebase_handler.get_all_items(
        collection=collection, 
        item_id=item_id
    )
    if item_data:
        return jsonify({
            "message": f"Retrieved {item_id} from {collection}: {data}", 
            "data": item_data
        }), 200
    else:
        return jsonify({
            "error": f"{item_id} not found in {collection}"
        }), 400

@app.route('/get-all-items', methods=['GET'])
def app_get_all_items():
    collection = "inventory"
    data = firebase_handler.get_all_items(collection=collection)
    if data:
        return jsonify({
            "message": f"Retrieved all items from {collection}: {data}", 
            "data": data
        }), 200
    else:
        return jsonify({
            "error": f"No items found in {collection}"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)