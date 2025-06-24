from django.urls import path
from .views import index, employee_list

urlpatterns = [
    path('', index, name='index'),  # Renders index.html
    path('api/employees/', employee_list, name='employee_list'),  # JSON API
]