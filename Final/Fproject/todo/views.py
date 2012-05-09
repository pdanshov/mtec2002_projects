# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
def todo(request):
    t = loader.get_template('todo/todo.html')
    d = {"greeting":"hello"}
    c = Context(d)
    return HttpResponse(t.render(c))