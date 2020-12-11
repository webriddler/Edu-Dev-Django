from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import headlines,events,subscription
from .forms import sub_form
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import auth
from django.contrib.auth.models import User


#Here we only define Function to be perform for having request from users

def head(request):
	duplicacy='none'  ##ALWAYS POSTING DATA IS ABOVE THAN GETING DATA
	subname=''
	subs=''
	if request.method=='POST':
		form=sub_form(request.POST)  #POSTING REQUEST TO THE SERVER VIA FORM
		subsdata=subscription.objects.all()
		if form.is_valid():  #CHECKING VALIDFATIONS
			data=form.cleaned_data #TAKING USER ENTERED DATA YET NOT SENT TO ADMIN
			subname=data['name']  #ACCESSING USER INPUT DATA IN FORM VIA NAME OF INPUT FIELD
			for sdata in subsdata:
				if sdata.email == data['email']:
					duplicacy='True'
					break
			if duplicacy == 'none':
				duplicacy='False'
				form.save()   #AT LAST SAVING DATA TO SERVER AFTER ALL VALIDATIONS
				form=sub_form()

		else:
			subs='False'
	else:
		form=sub_form()

	head_data=headlines.objects.all()
	st=0
	tc=0
	nf=0
	for a in range(0,len(head_data)):
		if head_data[a].day == 'Today':  #ACCESSING EACH DATA VIA INDEX OF A PARTICULAR
			if head_data[a].active == True:  #HERE FIELD IS ACTIVE
				if head_data[a].concern == 'Students':
					st=st+1
				elif head_data[a].concern == 'Teachers': #HERE FIELD IS CONCERN
					tc=tc+1
				else:
					nf=nf+1

	if not request.COOKIES.get('ck1'):			
		ck=datetime.now()
	else:
		ltime=request.COOKIES.get('ck1')
		ck=datetime.strptime(ltime[:-7], "%Y-%m-%d %H:%M:%S")				

	dtime=datetime.now() #FETCHING CURRENT TIME
	head_data=head_data.order_by('-created') #SORTING IN DESCENDING ORDER
	event_data=events.objects.all()
	lsmdet=event_data.order_by('-last_modified')[0] ##RESULTS IN Object not values
	event_data=event_data.order_by('date') #SORTING DATA IN ASCENDING ORDER
	context={'head_data':head_data,'dtime':dtime,'st':st,'tc':tc,'nf':nf,'event_data':event_data,
	'form':form,'duplicacy':duplicacy,'subname':subname,
	'subs':subs,'lsmdet':lsmdet,'ck':ck}
	

	return render(request,'index.html',context)
	
def logout(request):
	auth.logout(request)
	ck2=request.COOKIES.get('ck2')
	response=redirect("/")
	response.set_cookie('ck1',ck2,60*60*24*365)
	response.delete_cookie('user')
	return response
