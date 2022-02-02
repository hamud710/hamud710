from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    Name = models.CharField(max_length=100)
    Quotes = models.CharField(max_length=200)
    Email = models.EmailField()
    AboutUs = RichTextField()
    WhatDoWeDo = RichTextField()
    OurMission = RichTextField()
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100,blank=None,null=None)
    Phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to="MyImage/")

    