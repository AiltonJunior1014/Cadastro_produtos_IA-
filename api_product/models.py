from django.db import models

class Product(models.Model):
    product_code = models.CharField(max_length=100, primary_key=True, default='')
    product_name = models.CharField(max_length=100, default='')
    product_description = models.CharField(max_length=200, default='')
    product_measure = models.CharField(max_length=100, default='')
    product_price = models.CharField(max_length=100, default='')
    product_info = models.CharField(max_length=5000, default='')

    def __str__(self) -> str:
        return f'Code: {self.product_code} | Name: {self.product_name}'
# Create your models here.


class Produto():
    name = ""
    code = 0.0
    sku = ""
    shortDescription = ""   
    description = ""
    price = 0.0
    promotion_price = 0.0
    stock = 0
    minimun_stock = 0
    unit = ""
    weight = 0.0
    height = 0.0
    length = 0.0
    brand = ""
    modified = ""
    status = True
    ean = ""
    partCode = ""
    ncm = ""
    crossDockings = 0.0
    video = ""
    images = ""
    categories = []
    type
    items = []

    
    def __str__(self):
        return '{ "'"name"'": "'"Nome do Produto"'", "'"shortDescription"'": "Descrição curta", "description": "Descrição completa", "price": 106.39,
                "promotionalPrice": 0.0,"packagingQuantity": 1.0,"stock": 57.0,"stockFake": 1000,"minimumStock": 0.0,"unit": "PC","weight": 0.0,"height": 0.0,"width": 0.0,
                "length": 0.0,"brand": "teste","modifield": "2019-07-23 00:00:00","status": true,"ean": null,"partCode": "0024","ncm": "84834090","crossDocking": 0.0,"video": null,
                "images": null,"categories": [{"codeCategory":"20"}],"type": 2,"items": [] }"


    
    
