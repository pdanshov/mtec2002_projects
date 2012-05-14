from django.contrib import admin #Import the admin  
from models import TodoItem #Import our todo Model. 
admin.site.register(TodoItem) #Register the model with the admin  