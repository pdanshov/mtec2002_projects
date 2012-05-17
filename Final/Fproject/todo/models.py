from django.db import models
import datetime
# Create your models here.
class todoitem(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField(auto_now_add=True) #Like a DATETIME field
    completed = models.BooleanField(blank=True)
    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
    def __str__(self):
       return self.name
#    if self.completed:
#        stats.append('completed')
    class Admin:
        pass