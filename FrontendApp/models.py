from django.db import models

# Create your models here.
class signupDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    weight=models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    calorie_intake=models.IntegerField(null=True,blank=True)
class calorieDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    weight=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    calorie=models.IntegerField(null=True,blank=True)
class number_basis_foodDB(models.Model):
    item_name=models.CharField(max_length=100,null=True,blank=True)

class item_addedDB(models.Model):
    datepicker=models.DateField(max_length=250,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    calorie_intake=models.IntegerField(null=True,blank=True)
    name_added=models.CharField(max_length=100,null=True,blank=True)
    calorie_added=models.FloatField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    total_calorie=models.IntegerField(null=True,blank=True)
class final_dataDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    total=models.CharField(max_length=100,null=True,blank=True)
    day = models.CharField(max_length=250, null=True, blank=True)






