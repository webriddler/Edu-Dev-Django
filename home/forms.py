from django import forms
from .models import subscription

class sub_form(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control nameok mb-3'}),required=True,max_length=20,label='')
	email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control emailerror mb-2'}),required=True, label='')
	class Meta():
		model=subscription #The name of our model is subscription 	
		fields=[
			'name',
			'email'
		]  #Having all the Fields from Models 

class mob_sub_form(forms.ModelForm):
	email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'ml-0 mobilesubs'}),required=True, label='')
	class Meta():
		model=subscription #The name of our model is subscription 	
		fields=[
			'email'
		]  #Having all the Fields from Models 
