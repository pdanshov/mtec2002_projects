# Create your views here.
#from django.http import HttpResponse
#from django.template import Context, loader
from django.shortcuts import render_to_response
#from Fproject.todo.models import TodoList
from models import TodoItem

def TodoPage(request):
    items = TodoItem.objects.all()
    if request.method == "POST":
        #if action == "edit":
            try:
                litem = TodoItem.objects.get(id = request.POST['listid'])
                litem.completed = not litem.completed
                litem.save()
            except TodoItem.DoesNotExist:
                pass
    if request.method == "CREATE":
        try:
            litem = items(name=request.POST['name'], description=request.POST['description'])
            litem.save()
        except TodoItem.Exists:
            pass
    #t = loader.get_template('todo/todo.html')
    #d = {"greeting":"hello"}
    #c = Context(d)
    #return HttpResponse(t.render(c))
    return render_to_response('./todo/todo.html', {'items':items})