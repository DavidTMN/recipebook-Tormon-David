from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello World!")
# Create your views here.

def basicParams(request, num = 1):
    if num == 1:
        number = "first"
    elif num == 2:
        number = "second"
    else:
        number = "nth"
    return render(request, "basicParams.html", {"number":number})

def recipeList(request):
    ctx = {
        "Recipes": [
            "Recipe 1",
            "Recipe 2"
        ]
    }
    return render(request, "recipelist.html", ctx)