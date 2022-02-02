from django.db import models
from ckeditor.fields import RichTextField


class JewelleryCategory(models.Model):
   Name = models.CharField(max_length = 150)

   def __str__(self):
        return self.Name


class Item(models.Model):
    Category = models.ForeignKey(JewelleryCategory, on_delete=models.CASCADE)
    Name = models.CharField(max_length = 150)
    oldPrice = models.FloatField(default=0.0)
    Price = models.FloatField(default=0.0)
    Quantity = models.IntegerField(default=0)
    about = RichTextField(null = True)
    color = models.CharField(max_length=100,default='Gold')
    Image1 = models.ImageField(upload_to='JewelleryImages',null=True)
    Image2 = models.ImageField(upload_to='JewelleryImages',  blank=True, null=True )
    Image3 = models.ImageField(upload_to='JewelleryImages', blank=True, null=True)
    Image4 = models.ImageField(upload_to='JewelleryImages',  blank=True, null=True)

    def __str__(self):
        return self.Name

class Compare(models.Model):
    Name = models.ForeignKey(Item, on_delete=models.CASCADE  )

    def __str__(self):
        return self.Name.Name

class Cart(models.Model):
    Name = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.Name.Name

    
    
    
    