#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quote
from .serializers import QuoteSerializer

@api_view(['GET'])
def quote(request):
    if request.method == 'GET':
        from random import choice
        pks = Quote.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        quote = Quote.objects.filter(pk=random_pk)
        serializer = QuoteSerializer(quote, many=True)
        return Response(serializer.data)
