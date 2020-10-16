from django import forms
from .models import *

#Create forms here

class MovieForm(forms.ModelForm):

   class Meta:
        model = Movie
        fields = ('title','director','price','no_of_items')
