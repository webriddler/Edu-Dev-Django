from django import forms
from .models import help

class helpform(forms.ModelForm):
	subscriber=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control mb-1 wr '}),required=False)
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control wr '}),required=False,max_length=20)
	user=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Id','class':'form-control  wr'}),required=False,max_length=6)
	description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Have your concern here ?','class':'form-control','rows':2}),required=True,max_length=500)
	
	class Meta():
		model=help #The name of our model is subscription 	
		fields=[
			'subscriber',
			'user',
			'name',
			'description'
		]  #Having all the Fields from Models 
