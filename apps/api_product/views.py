from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
import json
import os
import google.generativeai as genai



class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    # Personalizando a resposta do GET por ID
    def retrieve(self, request, pk=None):
        produto = get_object_or_404(Product, pk=pk)
        serializer = self.get_serializer(produto)
        return Response({
            "mensagem": f"Detalhes do produto {product.nome}",
            "dados": serializer.data
        })


@api_view(['GET'])
def get_product(request):

    if request.method == 'GET':
        product = Product.objects.all()

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_product(request):
    
    if request.method == 'POST':
        nome_produto = request.GET.get('produto')
        new_product = request.data
        # serializer = ProductSerializer(data = new_product)

        prompt = f"""Preciso dos seguintes dados para cadastro do produto """+nome_produto+""".  with this schema:
        {{
            "code": "...",
            "name": "...",
            "shortDescription": "...",
            "description": "...",
            "price": ...,
            "promotionalPrice": ...,
            "packagingQuantity": ...,
            "stock": ...,
            "stockFake": 1000,
            "minimumStock": ..,
            "unit": "...",
            "weight": ...,
            "height": ...,
            "width": ...,
            "length": ...,
            "brand": "...",
            "modifield": "...",
            "status": ...,
            "ean": ...,
            "partCode": "...",
            "ncm": "...",
            "crossDocking": ...,
            "images": ...,
        }}
        """

        genai.configure(api_key=os.getenv('API_KEY'))
        model = genai.GenerativeModel("gemini-1.5-flash",generation_config={"response_mime_type": "application/json"})

        response = model.generate_content(prompt)

        print(response)
        return Response(response.text, status=status.HTTP_200_OK)
    
        
    return Response(status=status.HTTP_400_BAD_REQUEST)


