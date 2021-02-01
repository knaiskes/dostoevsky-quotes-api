from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('quotes/random', views.random, name='random'),
    path('quotes/', views.ApiQuoteListView.as_view(), name='quotes'),
    path('quotes/novel/<novel>', views.ApiQuoteListByNovelView.as_view(), name='quotes_by_novel'),
    path('quotes/<pk>', views.quote_by_id, name='quote_by_id'),
]
