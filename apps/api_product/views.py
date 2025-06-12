from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Produto
from .serializers import  MongoDBHandler
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from PIL import Image
from datetime import datetime,timedelta
from dotenv import load_dotenv
import json
import io
import re
import os
import uuid
import requests
import google.generativeai as genai

load_dotenv(override=True) 

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MongoDBHandler
    permission_classes = [IsAuthenticated]

    # Personalizando a resposta do GET por ID
    def retrieve(self, request, pk=None):
        produto = get_object_or_404(Product, pk=pk)
        serializer = self.get_serializer(produto)
        return Response({
            "mensagem": f"Detalhes do produto {product.nome}",
            "dados": serializer.data
        })

def getToken():
    hoje = datetime.now().date()
    diferenca = datetime.strptime(os.getenv('DATA_TOKEN'), "%Y-%m-%d").date() - hoje

    if diferenca.days < 365:
        return os.getenv('TOKEN_API')
    else:
        try:
            payload = json.dumps({
                "api_id": os.getenv('TOKEN_BRING'),  # Substitua pelo seu API ID
                "api_token": os.getenv('TOKEN_API')  # Substitua pelo seu API Token
            })
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
            token = requests.post(
                os.getenv('API_BRING')+'v1/auth',
                headers=headers,
                data=payload
            )
            os.environ['TOKEN_API'] = token.json().get("access_token")
            os.environ['DATA_TOKEN'] = datetime.now().strftime("%Y-%m-%d")
            return os.getenv('TOKEN_API')
        except Exception as e:
            print(f"Erro ao obter token: {e}")
            return None    

def criaProduto(dados):
    produto =  Produto()
    produto.set_code(dados.get('code', ''))
    produto.set_name(dados.get('name', ''))
    produto.set_shortDescription(dados.get('shortDescription', ''))
    produto.set_description(dados.get('description', ''))
    produto.set_price(dados.get('price', ''))
    produto.set_promotionalPrice(dados.get('promotionalPrice', ''))
    produto.set_packagingQuantity(dados.get('packagingQuantity', ''))
    produto.set_stock(dados.get('stock', ''))
    produto.set_stockFake(dados.get('stockFake', ''))
    produto.set_minimumStock(dados.get('minimumStock', ''))
    produto.set_unit(dados.get('unit', ''))
    produto.set_weight(dados.get('weight', ''))
    produto.set_height(dados.get('height', ''))
    produto.set_width(dados.get('width', ''))
    produto.set_length(dados.get('length', ''))
    produto.set_brand(dados.get('brand', ''))
    produto.set_modified(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))  
    produto.set_status(dados.get('status', ''))
    produto.set_ean(dados.get('ean', ''))
    produto.set_partCode(dados.get('partCode', ''))
    produto.set_ncm(dados.get('ncm', ''))
    produto.set_crossDocking(dados.get('crossDocking', ''))
    return produto

def salva_produto(produto):
        mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
        db_name = os.getenv('MONGO_DB_NAME', 'mydatabase')
        handler = MongoDBHandler(mongo_uri, db_name)
        return handler.save_produto(produto)

def enviaProduto(produto_dict):
    json_data = json.dumps(produto_dict, indent=4, ensure_ascii=False)
    token = getToken()
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    requests.request(
        "PUT",
        os.getenv('API_BRING')+'v1/products',
        headers=headers,
        data=json_data
        )

@api_view(['GET'])
def get_product(request):
    if request.method == 'GET':
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')
        mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
        db_name = os.getenv('MONGO_DB_NAME', 'mydatabase')
        handler = MongoDBHandler(mongo_uri, db_name)
        lista_produtos = handler.buscar_produtos_por_periodo(data_inicio, data_fim)
        print(f"Lista de produtos: {lista_produtos}")
        if lista_produtos:
            return Response(lista_produtos, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Nenhum produto encontrado."}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_product(request):
    if request.method == 'POST':
        nome_produto = request.data.get('produto')
        new_product = request.data
        # serializer = ProductSerializer(data = new_product)
        prompt = """Gere os dados para cadastrar o produto """+nome_produto+""" no formato JSON com as seguintes chaves:
                - code
                - name
                - shortDescription
                - description
                - price
                - promotionalPrice
                - packagingQuantity
                - stock
                - stockFake
                - minimumStock
                - unit
                - weight
                - height
                - width
                - length
                - brand
                - modified
                - status
                - ean
                - partCode
                - ncm
                - crossDocking
                - images (lista de URLs)
                Retorne APENAS o objeto JSON."""
        try:
            genai.configure(api_key=os.getenv('API_KEY'))
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                prompt
            )
            resposta = response.candidates[0].content.parts[0].text
            # Extrai apenas o JSON com regex
            match = re.search(r'{.*}', resposta, re.DOTALL)
            if match:
                clean_json = match.group(0)
                data = json.loads(clean_json)
                produto = criaProduto(data)
                salva_produto(produto)
                produto_dict = produto.to_dict()
                enviaProduto(produto_dict)
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        # print(response)
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_product_image(request):
    imagem = request.FILES['imagem']
    if imagem:
        try:
            imagem_bytes = imagem.read()
            image_data = io.BytesIO(imagem_bytes)
            img = Image.open(image_data)
            
            original_filename = imagem.name
            file_extension = os.path.splitext(original_filename)[1]
            unique_filename = f"produto_{uuid.uuid4().hex}{file_extension}"
            save_directory = os.path.join(settings.MEDIA_ROOT, 'uploads') 
            os.makedirs(save_directory, exist_ok=True)
            file_path = os.path.join(save_directory, unique_filename)
            img.save(file_path)

            prompt = """Gere os dados para cadastrar o produto segundo a imagem dele no formato JSON com as seguintes chaves:
                - code
                - name
                - shortDescription
                - description
                - price
                - promotionalPrice
                - packagingQuantity
                - stock
                - stockFake
                - minimumStock
                - unit
                - weight
                - height
                - width
                - length
                - brand
                - modified
                - status
                - ean
                - partCode
                - ncm
                - crossDocking
                - images (lista de URLs)
                Retorne APENAS o objeto JSON."""

            genai.configure(api_key=os.getenv('API_KEY'))
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content([
                prompt,
                img]
            )
            resposta = response.candidates[0].content.parts[0].text
            # Extrai apenas o JSON com regex
            match = re.search(r'{.*}', resposta, re.DOTALL)

            if match:
                clean_json = match.group(0)
                data = json.loads(clean_json)
                produto = criaProduto(data)
                salva_produto(produto)
                produto_dict = produto.to_dict()
                enviaProduto(produto_dict)  

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"erro": "Nenhuma imagem enviada."}, status=status.HTTP_400_BAD_REQUEST)