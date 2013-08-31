from models import Url

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ValidationError

import random

error_message =['Oops! ','Oh snap! ','Uh-oh! ']

def home(request):
	alert=[]
	if request.method=='POST':
		address=request.POST.get('uname',None)
		if (address):
			try :				
				obj=Url.objects.get(url=address)
				address=obj.shorturl				
				
			except Url.DoesNotExist:
				obj=Url(url=address)
				try:
					obj.clean_fields()
					obj.shortifyurl()
					obj.save()
					address=obj.shorturl
				except ValidationError, error:
					address=None
					alert=error.messages				
		else :
			alert.append('Please enter a URL.')		
		alert=[ random.choice(error_message) + i for i in alert ]		
		return render(request,'home.html',{'address':address,'alert':alert})
		
	
	else :
		return render(request,'home.html',{'alert':alert})



def redirect(request,key):
	if(key):
		key='/'+key
		try:
			ob=Url.objects.get(shorturl=key)
			val=ob.url
			ob.incr()
			ob.save()
			return HttpResponseRedirect(ob.url)
		except Url.DoesNotExist:
			key="Sorry! We couldn't find any url for that address!"			
			
	return render(request,'redir.html',{'key': key})
			
	
	
	