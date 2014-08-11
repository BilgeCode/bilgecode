from django.test import TestCase, Client
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from bilgecode.apps.passage_planner.models import Passage

class APITestCase(TestCase):
    
    def setUp(self):
        
        u1 = User.objects.create_user(username='user1', password='pass')
        u2 = User.objects.create_user(username='user2', password='pass')
        
        Passage.objects.create(user=u1, passage_data='{"name": "First Passage"}')
        Passage.objects.create(user=u2, passage_data='{"name": "Second Passage"}')

    def test_permissions(self):
        """
            Confirm that only the owner has access to change a passage
            and
            confirm that that change took place
        """
        c = Client()
        
        # confirm read access to the list of passages
        response = c.get('/api/passages/?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"id": 1, "owner": "user1",', response.content)
        self.assertIn('"id": 2, "owner": "user2",', response.content)
        
        # confirm that passage 1 is listed with the right owner and has read access
        response = c.get('/api/passages/1/?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"owner": "user1",', response.content)
        self.assertNotIn('"owner": "user2",', response.content)
        
        # change the passage with a POST request
        u1 = User.objects.get(username="user1")
        
        client = APIClient()
        client.force_authenticate(user=u1)
        
        response = client.get(
            '/api/passages/1/',
            format='json')
        self.assertEqual(response.status_code, 200)
        
        response = client.patch(
            '/api/passages/1/',
            {"passage_data": '{"name": "First Passage - modified"}'},
            format='json')
        self.assertEqual(response.status_code, 200)
        
        p1 = Passage.objects.get(user=u1)
        self.assertEqual(p1.passage_data['name'], "First Passage - modified")
        
        # confirm permission denied on other passage
        response = client.get(
            '/api/passages/2/',
            format='json')
        self.assertEqual(response.status_code, 200)
        
        response = client.patch(
            '/api/passages/2/',
            {"passage_data": '{"name": "Second Passage - modified"}'},
            format='json')
        self.assertEqual(response.status_code, 403)
