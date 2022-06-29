from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_employees', views.add_employees, name='add_employees'),
    path('edit_employee', views.edit_employee, name='edit_employee'),
    path('delete_employee', views.delete_employee, name='delete_employee'),
]
