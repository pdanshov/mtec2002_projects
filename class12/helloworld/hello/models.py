from django.db import models

# Create your models here.

#models is a filename, Model is the class - as is Charfield & BooleanField
class Todo(models.Model):
	name = models.CharField(max_length=200)
	finished = models.BooleanField()