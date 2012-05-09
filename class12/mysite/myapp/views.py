# Create your views here.
from myapp.models import Poll
from django.http import HttpResponse
from django.template import Context, loader
def test1(request):
    t = loader.get_template("test1/test1.html")
    l = ["One", "II", "Trinity"]
    d = {"list":l}
    c = Context(d)
    return HttpResponse(t.render(c))
def test2(request):
    t = loader.get_template("test2/test2.html")
    l = ["I", "Duo", "Terci"]
    #d = {"list":l, "Poll_list":models.Todo.objects.all()}
    d = {"list":l}
    c = Context(d)
    return HttpResponse(t.render(c))