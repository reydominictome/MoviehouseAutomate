from django import forms
from .models import *

#Create forms here

class CustomerForm(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields = ('first_name','last_name')