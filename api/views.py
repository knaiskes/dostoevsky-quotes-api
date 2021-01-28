#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .models import Quote
from .serializers import QuoteSerializer

@api_view(['GET'])
def quote(request):
    if request.method == 'GET':
        from random import choice
        pks = Quote.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        quote = Quote.objects.get(pk=random_pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

@api_view(['GET'])
def quote_by_id(request, pk):
     try:
         quote = Quote.objects.get(pk=pk)
     except Quote.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

     if request.method == 'GET':
         serializer = QuoteSerializer(quote)
         return Response(serializer.data)


class ApiQuoteListView(ListAPIView):
    serializer_class = QuoteSerializer
    #pagination_class = PageNumberPagination

    def get_queryset(self):
        return Quote.objects.all()

class ApiQuoteListByNovelView(ListAPIView):
    serializer_class = QuoteSerializer
    #pagination_class = PageNumberPagination

    def get_queryset(self):
        return Quote.objects.filter(novel=self.kwargs['novel'])
