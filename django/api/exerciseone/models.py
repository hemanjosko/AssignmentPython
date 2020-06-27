from django.db import models

# Create your models here.

class Router(models.Model):
    sapid = models.CharField(max_length=18)# iesSap sap:1/2/3:801
    hostname = models.CharField(max_length=14)# cisco2501
    loopback = models.CharField(max_length=15) # ipv4 127.0.0.1
    macaddress = models.CharField(max_length=17) # 00:11:22:aa:bb:cc
    is_deleted = models.IntegerField(default=0)