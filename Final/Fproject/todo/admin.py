from django.contrib import admin #Import the admin  
from models import TodoList #Import our todo Model. 
admin.site.register(TodoList) #Register the model with the admin  