from django.db import models

class Rockets_time_table(models.Model):
    rockets_name = models.CharField(max_length=500)
    launching_time = models.CharField(max_length=500)
    mission = models.CharField(max_length=500 ,default='')
    mission_url=models.CharField(max_length=10000 , default='')
    descrption=models.CharField(max_length=10000 , default='')
    image = models.ImageField(upload_to = 'rockets` image' , blank = True)



    ##a field of data of creation
    #created = models.DateTimeField(auto_now_add=True)
    ## a field of data of updating
    #updated = models.DateTimeField(auto_now=True)


# Create your models here.
