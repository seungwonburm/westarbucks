from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table='menus'

class Category(models.Model):
    name= models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE)
    class Meta:
        db_table = 'products_category'

class Drink(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    class Meta:
        db_table = 'products_drink' 

class Images(models.Model):
    image_url= models.CharField(max_length=1000)
    drink=models.ForeignKey(Drink, on_delete=models.CASCADE)

class Allergy(models.Model):
    name= models.CharField(max_length=50)
    class Meta:
        db_table='products_allergy'

class AllergyDrink(models.Model):
    allergy=models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink=models.ForeignKey(Drink, on_delete=models.CASCADE, null = True, default='')
    class Meta:
        db_table='products_allergydrink'
