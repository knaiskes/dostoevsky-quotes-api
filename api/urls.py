from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('quote/', views.quote, name='quote'),
    path('quotes/<pk>', views.quote_by_id, name='quote_by_id'),
]
