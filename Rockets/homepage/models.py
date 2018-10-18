from django.db import models

class Rockets_time_table(models.Model):
    rockets_name = models.CharField(max_length=500 ,default='____')
    lanuch_window = models.CharField(max_length=10000,default='____')
    launch_site = models.CharField(max_length=1000,default='____')
    description = models.CharField(max_length=1000000,default='____')
    month = models.CharField(max_length = 1000,default='____')

    image = models.ImageField(upload_to = 'rockets` image' ,null=True, blank=True,default='____')

    def  __str__(self):
        return self.rockets_name



class major_spaceports(models.Model):
    spaceport_name = models.CharField(max_length=100,default='____')
    country = models.CharField(max_length=1000,default='____')
    image= models.ImageField(upload_to = 'spaceport image' , blank=True,default='____')

    def  __str__(self):
        return self.spaceport_name

