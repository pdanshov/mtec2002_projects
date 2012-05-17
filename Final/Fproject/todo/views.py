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
				if request.POST['completed'] == "on":
					litem = todoitem.objects.get(id = request.POST['listid'])
					litem.completed = not litem.completed
					litem.save()
			except:
				print ""
			try:
				if request.POST['undone'] == "on":
					pass
			except:
				if request.POST['unchecked'] == "":
					litem = todoitem.objects.get(id = request.POST['listid'])
					litem.completed = not litem.completed
					litem.save()
			try:
				if request.POST['delete'] == "on":
					#cursor = connection.cursor()
					litem = todoitem.objects.get(id = request.POST['listid'])
					litem.delete()
			except:
				print ""
			print request.POST
			print request.POST['completed']
			#print "request.post completed %s" % (request.POST.getlist['completed'])
			#print "request.post delete %s" % (request.POST.getlist['delete'])
		except KeyError:
			print request.POST
			print "KeyError except"
			pass
	if request.method == "GET":
		print "PUT turns to GET"
		print request.GET
		print request.GET
		print request.GET['name']
		print request.GET['description']
		try:
			if request.GET['description'] != "":
				litem = todoitem(name=request.GET['name'], description=request.GET['description'])
				litem.save()
		except:
			print "Except Clause"
	#t = loader.get_template('todo/todo.html')
	#d = {"greeting":"hello"}
	#c = Context(d)
	#return HttpResponse(t.render(c))
	return render_to_response('./todo/todo.html', {'items':items})