from django.db import models
from settings import BASE_URL

import hashlib


class Url(models.Model):
	url=models.URLField(verify_exists=True,max_length=200,default=None,blank=False,unique=True)
	shorturl=models.URLField(null=True,blank=True)
	date=models.DateTimeField(auto_now_add=True)
	count=models.IntegerField(default=0)
	isspam=models.IntegerField(default=0)

	def __unicode__(self):
		return self.url

	def incr(self):
		self.count+=1

	def shortifyurl(self):
		self.shorturl= BASE_URL + hashlib.sha512(self.url).hexdigest()[:5]
	
	class Meta:
		app_label = u'short'