from django.shortcuts import render
from .forms import helpform
from home.models import subscription
from .models import help
from django.contrib.auth.models import User


def inshelp(request):
	wrongmail=''
	wronguser=''
	activsub=''
	nameval=''
	null=''
	again=''

	if request.method=='POST':
		form2=helpform(request.POST)
		if form2.is_valid():	
			data=form2.cleaned_data
			userdata=User.objects.all()
			if data['subscriber'] == '':
				if data['user'] != '' or data['name'] != '':
					for usd in userdata:
						if usd.username == data['user']:
							if usd.first_name == data['name'] :
								form2.save()   #AT LAST SAVING DATA TO SERVER AFTER ALL VALIDATIONS
								form2=helpform()
								wronguser='False'
							else:
								activsub='False'
								wronguser='True'
								nameval='Student Name is not Valid as per User Id'

						else:
							activsub='False'
							wronguser='True'
				else:
					null='True'

			else:
				count=0
				subsdata=subscription.objects.all()
				helpdata=help.objects.all()
				for sub in subsdata:
					if sub.email == data['subscriber']:
						for hesk in helpdata :
							if hesk.subscriber == data['subscriber'] and hesk.solved == False:
								count+=1
						if count>=2:
							again = 'True'
							wrongmail=''
							break
						else:
							wrongmail='False'
							form2.save()
							form2=helpform()
							break
					else:
						wrongmail='True'
						activsub='True'

		else:
			wrongmail='True'

	else:
		form2=helpform()
	
	context={'form2':form2,'wronguser':wronguser,
	'wrongmail':wrongmail,'activsub':activsub,'nameval':nameval,'null':null,'again':again}
	return render(request,'help.html',context)
