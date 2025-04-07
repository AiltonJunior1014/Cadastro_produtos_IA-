from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import os
import jwt


@api_view(['GET'])
def gerar_JWT(request):
    if request.method == 'GET':


    return Response(status=status.HTTP_400_BAD_REQUEST)


