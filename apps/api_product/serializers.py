from pymongo import MongoClient
from models import Produto


class MongoDBHandler:
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.produtos_collection = self.db['produtos'] 

    def save_produto(self, produto: Produto):
        """Salva um objeto Produto no MongoDB."""
        produto_dict = produto.to_dict()
        result = self.produtos_collection.update_one(
            {'code': produto_dict['code']}, 
            {'$set': produto_dict},          
            upsert=True                      
        )
        if result.upserted_id:
            print(f"Produto '{produto.name}' inserido com _id: {result.upserted_id}")
        elif result.modified_count > 0:
            print(f"Produto '{produto.name}' atualizado.")
        else:
            print(f"Produto '{produto.name}' já existia e não foi modificado.")
        return result

    def get_produto_by_code(self, code: str):
        """Busca um produto pelo código."""
        doc = self.produtos_collection.find_one({'code': code})
        if doc:
            return Produto(**doc) 
        return None