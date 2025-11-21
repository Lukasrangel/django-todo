from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks),
    path('newtask', views.newTask),
    path('task/<int:id>', views.viewTask),
    path('edit/<int:id>', views.editTask),
    path('delete/<int:id>', views.deleteTask),
    path('delete/<int:id>', views.deleteTask),
    path('changestatus/<int:id>', views.changestatus),
    path('mail', views.mail),
]