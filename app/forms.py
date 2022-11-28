from django.forms import forms
from . models import *
from django.forms import ModelForm

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
