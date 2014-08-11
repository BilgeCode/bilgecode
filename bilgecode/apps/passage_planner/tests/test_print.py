from django.test import TestCase

from django.contrib.auth.models import User
from bilgecode.apps.passage_planner.models import Passage

from datetime import date

class PrintTestCase(TestCase):
    
    def setUp(self):
        u1 = User.objects.create(username="user1")
        u2 = User.objects.create(username="user2")
        
        Passage.objects.create(user=u1, passage_data='{"name": "First Passage"}')
        Passage.objects.create(user=u2, passage_data='{"notname": "Second Passage"}')

    def test_output_string(self):
        """Confirm that the string representation is working properly"""
        
        u1 = User.objects.get(username="user1")
        u2 = User.objects.get(username="user2")
        
        p1 = Passage.objects.get(user=u1)
        p2 = Passage.objects.get(user=u2)
        
        self.assertEqual(p1.__unicode__(), u"First Passage")
        # confirm that the current year is in the output for the empty one
        self.assertIn(str(date.today().year), p2.__unicode__())
