# Create your views here.
#from django.http import HttpResponse
#from django.template import Context, loader
from django.shortcuts import render_to_response
#from Fproject.todo.models import todolist
from models import todoitem
from django.db import transaction
#from django.db import connection

def todopage(request):
	items = todoitem.objects.all()
	if request.method == "POST":
		try:
			try:
				if request.POST['completed'] == "on" and request.POST['checked'] == "":
					litem = todoitem.objects.get(id = request.POST['listid'])
					litem.completed = not litem.completed
					litem.save()
					print "first"
			except:
				print "first exception"
			try:
				if request.POST['completed'] == "" and request.POST['notchecked'] == "":
					pass
			except:
				litem = todoitem.objects.get(id = request.POST['listid'])
				litem.completed = not litem.completed
				litem.save()
				print "second"
			try:
				if request.POST['delete'] == "on":
					#cursor = connection.cursor()
					litem = todoitem.objects.get(id = request.POST['listid'])
					litem.delete()
					#litem.save()
					print "delete"
			except:
				pass
			#print "request.post completed %s" % (request.POST['completed'])
			#print "request.post delete %s" % (request.POST['delete'])
		except KeyError:
			pass
	if request.method == "GET":
		print "PUT turns to GET"
		try:
			print request.GET
			print request.GET
			print request.GET['name']
			print request.GET['description']
			litem = todoitem(name=request.GET['name'], description=request.GET['description'])
			litem.save()
		except:
			print "Except Clause"
	#t = loader.get_template('todo/todo.html')
	#d = {"greeting":"hello"}
	#c = Context(d)
	#return HttpResponse(t.render(c))
	return render_to_response('./todo/todo.html', {'items':items})