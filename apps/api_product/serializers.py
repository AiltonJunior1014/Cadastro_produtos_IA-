from pymongo import MongoClient
from .models import Produto
from datetime import datetime


class MongoDBHandler:
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.produtos_collection = self.db['produtos'] 

    def save_produto(self, produto: Produto):
        """Salva um objeto Produto no MongoDB."""
        produto_dict = produto.to_dict()
        try:
            result = self.produtos_collection.update_one(
                {'code': produto_dict['code']}, 
                {'$set': produto_dict},          
                upsert=True                      
            )
            if result.upserted_id:
                print(f"Produto '{produto._name}' inserido com _id: {result.upserted_id}")
            elif result.modified_count > 0:
                print(f"Produto '{produto._name}' atualizado.")
            else:
                print(f"Produto '{produto._name}' já existia e não foi modificado.")
            return result
        except Exception as e:
                print(f"Erro ao salvar produto: {e}")
                return None

    def get_produto_by_code(self, code: str):
        """Busca um produto pelo código."""
        doc = self.produtos_collection.find_one({'code': code})
        if doc:
            return Produto(**doc) 
        return None
    
    def buscar_produtos_por_periodo(self, data_inicio, data_fim):
        data_inicio_iso = datetime.strptime(data_inicio, "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")
        data_fim_iso = datetime.strptime(data_fim, "%Y-%m-%d").strftime("%Y-%m-%dT23:59:59Z")

        query = {
            "modified": {
                "$gte": data_inicio_iso,
                "$lte": data_fim_iso
            }
        }

        produtos = list(self.produtos_collection.find(query))
        for produto in produtos:
            produto['_id'] = str(produto['_id'])
        return produtos