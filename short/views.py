from models import Url

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ValidationError

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
			alert.append('Please use a valid URL!')		

		return render_to_response('home.html',{'address':address,'alert':alert},context_instance=RequestContext(request))
		
	
	else :
		return render_to_response('home.html',{'alert':alert},context_instance=RequestContext(request))



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
			
	return render_to_response('redir.html',{'key':key},context_instance=RequestContext(request))
			
	
	
	