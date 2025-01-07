from django.test import TestCase
from .models import Account
from django.contrib.auth.models import User



class PostModelTest(TestCase):
    def setup(self):
        self.account=Account.objects.create(user=User.objects.get(id=3))


    def test_post_creation(self):
        self.assertEqual(self.post.title,'test')
        self.assertEqual(self.post.description,'this is a test')

    def test_post_string_representation(self):
        self.assertEqual(str(self.post),'test')
        
# Create your tests here.
