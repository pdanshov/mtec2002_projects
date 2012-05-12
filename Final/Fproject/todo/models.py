from django.db import models
# Create your models here.
class TodoList(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
    completed = models.BooleanField()
    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
    #def __str__(self):
    #   return self.name
    class Admin:
        pass