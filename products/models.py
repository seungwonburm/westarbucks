from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table='menus'

class Categories(models.Model):
    name= models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE)
    class Meta:
        db_table = 'products_category'

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6,decimal_places =2) 
    sodium_mg = models.DecimalField(max_digits=6,decimal_places =2)
    saturated_fat_g = models.DecimalField(max_digits=6,decimal_places =2)
    sugars_g = models.DecimalField(max_digits=6,decimal_places =2)
    protein_g = models.DecimalField(max_digits=6,decimal_places =2)
    caffeine_mg= models.DecimalField(max_digits=6,decimal_places =2)
    size_ml = models.CharField(max_length = 45)
    size_fluid = models.CharField(max_length = 45)

    class Meta:
        db_table = 'nutritions'


class Products(models.Model):
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length = 50, null = True, default='')
    description = models.TextField(null = True, default='')
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    nutrition = models.ForeignKey(Nutritions, on_delete= models.CASCADE)

    class Meta:
        db_table = 'products_drink' 


class Images(models.Model):
    image_url= models.CharField(max_length=2000)
    drink=models.ForeignKey(Products, on_delete=models.CASCADE)
    class Meta:
        db_table = 'url'

class Allergy(models.Model):
    name= models.CharField(max_length=50)
    class Meta:
        db_table='products_allergy'

class Allergy_Products(models.Model):
    allergy=models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink=models.ForeignKey(Products, on_delete=models.CASCADE, null = True, default='')
    class Meta:
        db_table='products_allergydrink'
