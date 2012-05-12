# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
#from Fproject.todo.models import TodoList
from models import TodoList

def TodoPage(request):
    items = TodoList.objects.all()
    if request.method == "POST":
        try:
            litem = TodoList.objects.get(id = request.POST['listid'])
            litem.completed = not litem.completed
            litem.save()
        except TodoList.DoesNotExist:
            pass
    #t = loader.get_template('todo/todo.html')
    #d = {"greeting":"hello"}
    #c = Context(d)
    #return HttpResponse(t.render(c))
    return render_to_response('./todo/todo.html', {'items':items})