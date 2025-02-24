from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello World!")
# Create your views here.

def recipeOne(request):
    ctx = {
        "name": "Recipe 1",
    "ingredients": [
        {
            "name": "tomato",
            "quantity": "3pcs"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "pork",
            "quantity": "1kg"
        },
        {
            "name": "water",
            "quantity": "1L"
        },
        {
            "name": "sinigang mix",
            "quantity": "1 packet"
        }
    ],
    "link" :  "/recipe/1"
    }
    
    return render(request, "recipelist.html", ctx)

def recipeList(request):
    ctx = {
        "Recipes": [
            "Recipe 1",
            "Recipe 2"
        ]
    }
    return render(request, "recipelist.html", ctx)