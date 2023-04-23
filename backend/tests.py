from unittest import TestCase
from backend.models import Url

# test data
test_data = [{
    "url": "https://www.yahoo.com/"
    }
]

class UrlTestCase(TestCase):

    def setUp(self):
        # create instance of model
        for test_product in test_data:
            url = Url(**test_product)
            url.save()

    def test_product_database(self):
        url = Url.objects.get(url='https://www.yahoo.com/')
        self.assertTrue(True)

    '''def test_product_view_all(self):
        response = self.client.get('/shop/products', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 3)
    
    
    def test_product_view_with_id(self):
        response = self.client.get('/shop/products?id=1', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['title'], 'prod_1')
    
    
    def test_product_view_with_min(self):
        response = self.client.get('/shop/products?min_price=2.0', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['title'], 'prod_2')
    
    
    def test_product_view_with_max(self):
        response = self.client.get('/shop/products?max_price=2.0', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['title'], 'prod_1')
    
    
    def test_product_view_with_min_and_max(self):
        response = self.client.get('/shop/products?min_price=2.0&max_price=11.0', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['title'], 'prod_2')
    
    
    def test_product_view_with_category(self):
        response = self.client.get('/shop/products?category=cat_2', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['title'], 'prod_2')
    
    
    def test_product_view_with_non_exsiting_id(self):
        response = self.client.get('/shop/products?id=4', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 0)'''