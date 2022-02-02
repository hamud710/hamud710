from .models import *
from django.forms import ModelForm




class cartmodel(ModelForm):
    class Meta:
        model = Cart
        fields = ['Name']


