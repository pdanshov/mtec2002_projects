from django.contrib import admin #Import the admin  
from models import todoitem #Import our todo Model. 
admin.site.register(todoitem) #Register the model with the admin  