from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .models import Produto
from .serializers import ProductSerializer
import json
import os
import google.generativeai as genai



@api_view(['GET'])
def get_product(request):

    if request.method == 'GET':
        product = Product.objects.all()

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def post_product(request):
    
    if request.method == 'GET':
        new_product = request.data
        serializer = ProductSerializer(data = new_product)
        p = Produto()
        
        genai.configure(api_key=os.getenv('API_KEY'))
        model = genai.GenerativeModel("gemini-1.5-flash",generation_config={"response_mime_type": "application/json"})

        response = model.generate_content("Preciso da descrição completa para cadastro de molho de tomate fugini 300g.  with this schema:")

        print(p)
        return Response(response.text, status=status.HTTP_200_OK)
    
        
    return Response(status=status.HTTP_400_BAD_REQUEST)


