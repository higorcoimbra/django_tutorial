from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	email 		= models.EmailField()
	#blank nulo no formulario e null nulo no BD
	full_name 	= models.CharField(max_length=120,blank=True,null=True) 
	#auto_now_add -> quando for criado, salve o tempo.
	#auto_now -> quando for alterado e salvo, save o tempo (ha qualquer hora).
	timestamp 	= models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.email