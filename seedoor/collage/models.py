from django.db import models

# Create your models here.
class Student(models.Model):

	reg_number 			= models.CharField(max_length=50, null=False, blank=False, unique=True)
	ein_1               = models.CharField(max_length=6, null=False, blank=True)
	ein_2               = models.CharField(max_length=6, null=False, blank=True)
	ein_3               = models.CharField(max_length=6, null=False, blank=True)
	nid          	    = models.CharField(max_length=17, null=False, blank=True, unique=True)
	amount              = models.CharField(max_length=10, null=False, blank=True)
	
	
	def __str__(self):
		return self.reg_number