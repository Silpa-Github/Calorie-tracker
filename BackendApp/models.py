from django.db import models

# Create your models here.
class fooditemDB(models.Model):
    food_name=models.CharField(max_length=100,null=True,blank=True)
    food_calorie=models.IntegerField(null=True,blank=True)
    food_image=models.ImageField(upload_to='food_images',null=True,blank=True)

class number_basis_foodDB(models.Model):
    item_name=models.CharField(max_length=100,null=True,blank=True)

class number_basis_calorieDB(models.Model):
     item=models.CharField(max_length=100,null=True,blank=True)
     small=models.IntegerField(null=True,blank=True)
     medium=models.IntegerField(null=True,blank=True)
     large=models.IntegerField(null=True,blank=True)
     item_image = models.ImageField(upload_to='item_images', null=True, blank=True)

class nutrientsDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    calorie=models.FloatField(null=True,blank=True)
    carbohydrates=models.FloatField(null=True,blank=True)
    fiber=models.FloatField(null=True,blank=True)
    protein=models.FloatField(null=True,blank=True)
    fat=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to='nutrientimg',null=True,blank=True)
