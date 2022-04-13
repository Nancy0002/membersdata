from django.db import models

# Create your models here.
class member(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Sex = models.CharField(max_length=2, default='M', null=False)
	Birthday = models.DateField(null=False)
	Email = models.EmailField(max_length=100, blank=True, default='')
	Phone = models.CharField(max_length=50, blank=True, default='')
	Addr = models.CharField(max_length=255,blank=True, default='')
	
	def __str__(self):
		return self.Name
