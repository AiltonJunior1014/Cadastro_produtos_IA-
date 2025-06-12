from django.db import models

import os
import datetime

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


class Produto(models.Model):
    def __init__(self):
        self._code = ''
        self._name = None
        self._shortDescription = None
        self._description = None
        self._price = None
        self._promotionalPrice = None
        self._packagingQuantity = None
        self._stock = None
        self._stockFake = None
        self._minimumStock = None
        self._unit = None
        self._weight = None
        self._height = None
        self._width = None
        self._length = None
        self._brand = None
        self._modified = None
        self._status = None
        self._ean = None
        self._partCode = None
        self._ncm = None
        self._crossDocking = None

    def to_dict(self):
        return {
        'code': self._code,
        'name': self._name,
        'shortDescription': self._shortDescription,
        'description': self._description,
        'price': self._price,
        'promotionalPrice': self._promotionalPrice,
        'packagingQuantity': self._packagingQuantity,
        'stock': self._stock,
        'stockFake': self._stockFake,
        'minimumStock': self._minimumStock,
        'unit': self._unit,
        'weight': self._weight,
        'height': self._height,
        'width': self._width,
        'length': self._length,
        'brand': self._brand,
        'modified': self._modified,
        'status': self._status,
        'ean': self._ean,
        'partCode': self._partCode,
        'ncm': self._ncm,
        'crossDocking': self._crossDocking
        }


    
    
    # Getters and Setters
    def get_code(self): return self._code
    def set_code(self, value): self._code = value

    def get_name(self): return self._name
    def set_name(self, value): self._name = value

    def get_shortDescription(self): return self._shortDescription
    def set_shortDescription(self, value): self._shortDescription = value

    def get_description(self): return self._description
    def set_description(self, value): self._description = value

    def get_price(self): return self._price
    def set_price(self, value): self._price = value

    def get_promotionalPrice(self): return self._promotionalPrice
    def set_promotionalPrice(self, value): self._promotionalPrice = value

    def get_packagingQuantity(self): return self._packagingQuantity
    def set_packagingQuantity(self, value): self._packagingQuantity = value

    def get_stock(self): return self._stock
    def set_stock(self, value): self._stock = value

    def get_stockFake(self): return self._stockFake
    def set_stockFake(self, value): self._stockFake = value

    def get_minimumStock(self): return self._minimumStock
    def set_minimumStock(self, value): self._minimumStock = value

    def get_unit(self): return self._unit
    def set_unit(self, value): self._unit = value

    def get_weight(self): return self._weight
    def set_weight(self, value): self._weight = value

    def get_height(self): return self._height
    def set_height(self, value): self._height = value

    def get_width(self): return self._width
    def set_width(self, value): self._width = value

    def get_length(self): return self._length
    def set_length(self, value): self._length = value

    def get_brand(self): return self._brand
    def set_brand(self, value): self._brand = value

    def get_modified(self): return self._modified
    def set_modified(self, value): self._modified = value

    def get_status(self): return self._status
    def set_status(self, value): self._status = value

    def get_ean(self): return self._ean
    def set_ean(self, value): self._ean = value

    def get_partCode(self): return self._partCode
    def set_partCode(self, value): self._partCode = value

    def get_ncm(self): return self._ncm
    def set_ncm(self, value): self._ncm = value

    def get_crossDocking(self): return self._crossDocking
    def set_crossDocking(self, value): self._crossDocking = value
