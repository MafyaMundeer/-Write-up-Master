from django.conf import settings
from django.db import models

class Person(models.Model):
	
	name = models.CharField(max_length=30)
	about = models.TextField()
	slug = models.SlugField(max_length=30)
	photo = models.ImageField(default = 'default.png', blank = True)
	def __str__(self):
		return self.name
	def snippet(self):
		return (self.about[:20] + "...")




