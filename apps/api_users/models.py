from django.db import models


class User(models.Model):
    user_code = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100, default='')
    user_password = models.CharField(max_length=30, default='')

    def __str__(self) -> str:
        return f'Code: {self.user_code} | Name: {self.user_name}'



# Create your models here.

