import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os

load_dotenv()

firebase_cred_path = os.getenv("FIREBASE_CRED_PATH")
firebase_db_url = os.getenv("FIREBASE_DB_URL")

class FirebaseHandler:
    def __init__(self):
        return
    
    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_cred_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': firebase_db_url,
        })
    
    def add_item(self, collection, item_id, data):
        ref = db.reference(f'/{collection}/{item_id}')
        ref.set(data)
        print(f'Added {item_id} to {collection}')
    
    def get_item(self, collection, item_id):
        ref = db.reference(f'/{collection}/{item_id}')
        data = ref.get()
        if data:
            print(f"Retrieved {item_id} from {collection}: {data}")
            return data
        else:
            print(f"{item_id} not found in {collection}")
            return None
    
    def update_item(self, collection, item_id, updates):
        ref = db.reference(f'/{collection}/{item_id}')
        ref.update(updates)
        print(f"Updated {item_id} in {collection}")
    
    def delete_item(self, collection, item_id):
        ref = db.reference(f'/{collection}/{item_id}')
        ref.delete()
        print(f"Deleted {item_id} from {collection}")
    
    def get_all_items(self, collection):
        ref = db.reference(f'/{collection}')
        data = ref.get()
        if data:
            print(f"Retrieved all items from {collection}: {data}")
            return data
        else:
            print(f"No items found in {collection}")
            return {}