from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('quote/', views.quote, name='quote'),
]
