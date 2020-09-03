from django.urls import path
from ninth_app import views

urlpatterns = [
    path('', views.users, name='users')
]
