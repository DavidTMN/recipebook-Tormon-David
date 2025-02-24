from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")
# Create your views here.

def basicTemplate(request):
    return render(request, "basicParams.html")