#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quote
from .serializers import QuoteSerializer

@api_view(['GET'])
def quote(request):
    if request.method == 'GET':
        # TODO: get random quote
        quote = Quote.objects.filter(id=1)
        serializer = QuoteSerializer(quote, many=True)
        return Response(serializer.data)
