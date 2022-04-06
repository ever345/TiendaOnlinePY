from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('nuevo',views.create, name='create'),
]