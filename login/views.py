from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from datetime import datetime

def login(request):
	if not request.COOKIES.get('user'):
		login=''
		pwd=''
		suspended='False'
		context={}
		if request.method == 'POST':
			usname=request.POST['userid']
			passwd=request.POST['password']

			validate=auth.authenticate(username=usname,password=passwd)
			alluser = User.objects.all()
			for user in alluser:
					if user.username == usname:
						pwd='fail'
						break

			if validate is not None:
				if user.is_active:
					if user.is_staff :
						return redirect('/')
					else:
						auth.login(request,validate)
						response=redirect('studentpanel')
						response.set_cookie('user',usname,60*60*24*365)	
						if not request.COOKIES.get('ck1'):
							response.set_cookie('ck1',datetime.now(),60*60*24*365)
							response.set_cookie('ck2',datetime.now(),60*60*24*365)
							return response
						else:
							response.set_cookie('ck2',datetime.now(),60*60*24*365)
							return response
				else:
					suspended='True'
					return render(request,'login.html',context)

			else:
				login='fail'
				context={'login':login,'pwd':pwd}
				return render(request,'login.html',context)

		else:
			return render(request,'login.html')

	else:
		return redirect('/')




