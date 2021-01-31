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
        url = reverse('api:random')
        quote = Quote.objects.get(id=1)
        serializer = QuoteSerializer(quote)
        response = self.client.get(url, format='json')

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetQuoteById(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_quote = Quote.objects.create(text='test', novel='test')

    def test_get_quote_by_id(self):
        url =  reverse('api:quote_by_id', kwargs={'pk': self.test_quote.pk})
        quote = Quote.objects.get(pk=self.test_quote.pk)
        serializer = QuoteSerializer(quote)
        response = self.client.get(url, format='json')

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_quote_by_id(self):
        url =  reverse('api:quote_by_id', kwargs={'pk': 10})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetQuotesByNovel(APITestCase):
    def setUp(self):
        self.client = APIClient()
        Quote.objects.create(text='test1', novel='test')
        Quote.objects.create(text='test2', novel='test')
        Quote.objects.create(text='test3', novel='test')
        Quote.objects.create(text='test4', novel='test')
        Quote.objects.create(text='test5', novel='test')
        Quote.objects.create(text='test6', novel='test')
        Quote.objects.create(text='test7', novel='test')
        Quote.objects.create(text='test8', novel='test')
        Quote.objects.create(text='test9', novel='test')

    def test_get_valid_quotes_by_novel(self):
        import json
        url = reverse('api:quotes_by_novel', kwargs={'novel': 'test'})
        response = self.client.get(url)
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
