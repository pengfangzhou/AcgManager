from django.http import HttpResponse

# Create your views here.
def test(request):
    print "test()"
    return HttpResponse("Hello world!")