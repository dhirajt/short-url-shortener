from django.db import models
import hashlib


class Url(models.Model):
	url=models.URLField(verify_exists=True,max_length=200,blank=False,null=False)
	shorturl=models.URLField(null=True)
	date=models.DateTimeField(auto_now_add=True)
	count=models.IntegerField(default=0)

	def __unicode__(self):
		return self.url
	def incr(self):
		self.count+=1
	def shortifyurl(self):
		self.shorturl='/'+hashlib.sha512(self.url).hexdigest()[:5]
	
	class Meta:
		app_label = u'short'
		
		
		
