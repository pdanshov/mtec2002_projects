# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from hello import todo

def index(request):
	t = loader.get_template("hello/index.html")
	l = ["One", "Two", "Trinity"]
	dd = {"greeting":"hello", "gk":"gv", "three":"trinity"}
	d = {"greeting":"hello", "gk":"gv", "three":"trinity", "my_list":l, "dict":dd, 't':models.Todo.objects.all()}
	c = Context(d)
	return HttpResponse(t.render(c))

def howdy(request):
	t = loader.get_template("hello/howdy.html")
	d = {}
	c = Context(d)
	return HttpResponse(t.render(c))