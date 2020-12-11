from django.db import models
from django.utils import timezone

class help(models.Model):
	subscriber=models.EmailField(max_length=30,blank=True,default='Student')
	if subscriber == 'Student':
		user=models.CharField(max_length=6,blank=False)
		name=models.CharField(blank=False,max_length=20,help_text="Name should be Valid as per User Id")
	else:
		user=models.CharField(max_length=6,blank=True)
		name=models.CharField(blank=True,max_length=20,help_text="Name should be Valid as per User Id")
	
	description=models.TextField(blank=False,help_text="Related Concern",max_length=500)
	date=models.DateTimeField(auto_now_add=True)
	solved=models.BooleanField(default=False)
	class Meta:
		verbose_name_plural = 'Instant Help'



