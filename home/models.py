from django.db import models
#Remember here we define Classes only to be shown on server side
from django.utils import timezone
from datetime import datetime,timedelta
from django.contrib.auth.admin import User
from django.conf import settings
import request

class headlines(models.Model):
	concern_choices=(
		('Students','Students'),
		('Teachers','Teachers'),
		('Notification','Notification'),
		('Alert','Alert'),
		('Headline','Headline'),
		)
	concern=models.CharField(max_length=20,choices=concern_choices,default='Students',help_text="For whom the Articles belongs to.")
	if concern == 'Headline':
		title=models.CharField(unique_for_date='created',blank=False,max_length=100,help_text="Title should be unique for a Day")
		image=models.URLField(blank=True,help_text="Minimum Resolution 1000X800 ")
		description=models.TextField(blank=True,editable=False)
	else: 
		title=models.CharField(unique_for_date='created',blank=False,max_length=100,help_text="Title should be unique for a Day")
		description=models.TextField(blank=False,help_text="Short Description favourable Max Lenght 250 Characters",max_length=500)
		image=models.URLField(blank=True,help_text="Minimum Resolution 1000X800 ")
		created=models.DateTimeField(auto_now_add=True)
	last_modified=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)
	author=models.ForeignKey(primary_key=False,to=User,on_delete=models.SET_DEFAULT,default=1)
	
	
	@property
	def ago(self):
		diff=timezone.now()-self.created
		diff=str(diff)
		diff=diff[::-1]
		diff=diff[7::]
		diff=diff[::-1]
		return diff
	@property
	def day(self):  #Not under user control but can be accessed in templates
		todaydate=datetime.now().date()
		if todaydate == self.created.date():
			strtime='Today'
			return strtime
		elif todaydate-timedelta(days=1) == self.created.date() :
			strtime='Yesterday'
			return strtime
		else:
			strtime='Older'
			return strtime

	# @property
	# def author(self):
	# 	response=self.COOKIES['login']
	# 	return response
		
	class Meta:
		verbose_name_plural = 'Headlines'


class events(models.Model):
	event_name=models.CharField(blank=False,max_length=50,help_text='Event Name should be Short')
	date=models.DateField(blank=False)
	active=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	last_modified=models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Coming Events'


class subscription(models.Model):
	name=models.CharField(max_length=15,blank=False)
	email=models.EmailField(blank=False)
	created=models.DateTimeField(auto_now_add=True)
	active=models.BooleanField(default=True)
	class Meta:
		verbose_name_plural = 'Subscribers'

