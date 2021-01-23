from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from api.models import Quote
from api.serializers import QuoteSerializer

class GetSingleRandomQuote(APITestCase):
    def setUp(self):
        self.client = APIClient()
        Quote.objects.create(text='test', novel='test')

    def test_get_single_random_quote(self):
        url = reverse('api:quote')
        quote = Quote.objects.filter(id=1)
        serializer = QuoteSerializer(quote, many=True)
        response = self.client.get(url, format='json')

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
