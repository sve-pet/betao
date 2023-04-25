import json

from django.test import TestCase
from backend.models import Link

# test data
test_data = [
    {
        "link": "https://www.dn.se"
    },
    {
        "link": "https://api.le-systeme-solaire.net",
    },
    {
        "link": "https://www.yahoo.com"
    },
]


class UrlTestCase(TestCase):

    def setUp(self):
        for test_product in test_data:
            link = Link(**test_product)
            link.save()

    def test_link_database(self):
        link = Link.objects.get(link='https://api.le-systeme-solaire.net')
        self.assertEqual(link.score, 0)
        self.assertEqual(link.upvotes, 0)
        self.assertEqual(link.downvotes, 0)

    def test_link_view_all(self):
        response = self.client.get('/api/links', follow=True)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['link'], 'https://api.le-systeme-solaire.net')
        self.assertTrue(True)

    def test_link_view_with_id(self):
        response = self.client.get('/api/links/3/', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response['link'], 'https://www.yahoo.com')

    def test_link_upvote(self):
        link = Link.objects.get(pk=1)
        link.score = 0
        link.upvotes = 0
        link.save()
        self.client.post(path='/api/links/1/upvote', data={}, format='json', follow=True)
        response = self.client.get('/api/links/1', follow=True)
        self.assertEqual(response.data['score'], 1)
        self.assertEqual(response.data['upvotes'], 1)

    def test_link_downvote(self):
        link = Link.objects.get(pk=1)
        link.score = 1
        link.downvotes = 0
        link.save()

        self.client.post(path='/api/links/1/downvote', data={}, format='json', follow=True)
        response = self.client.get('/api/links/1', follow=True)
        self.assertEqual(response.data['score'], 0)
        self.assertEqual(response.data['downvotes'], 1)

