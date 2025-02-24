from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name = "home"),
    path("tasks/", views.tasks, name = "tasks"),
    path("basic/<int:num>", views.basicParams, name="basicParams")
]

app_name = "ledger"