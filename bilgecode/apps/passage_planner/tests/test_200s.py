from django.test import TestCase, Client

from django.contrib.auth.models import User
from bilgecode.apps.passage_planner.models import Passage

class PageResponseTests(TestCase):
    """
        Test that each view produces a 200 response.
    """
    
    def setUp(self):
        
        self.client = Client()
        
        u = User.objects.create(username="user")
        p = Passage.objects.create(user=u, passage_data='{"name": "Test Passage"}')
        self.hash_key = p.hash_key

    def test_pages(self):
        response = self.client.get('/passage-planner/')
        self.assertEqual(response.status_code, 200)
