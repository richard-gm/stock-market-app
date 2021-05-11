from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient


User = get_user_model()

class AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.userb = User.objects.create_user(username='cfe-2', password='somepassword2')

    def test_login_view(self):
        context = {  # using form dictionary - build in feature from django
            "btn_label": "Login",
            "title": "Login"
        }
        response = self.client.get('/admin/login/', context)

    def test_logout_view(self):
        context = {
            "description": "Are you sure you want to logout?",
            "btn_label": "Click to Confirm",
            "title": "Logout"
        }
        response = self.client.get('/admin/logout/', context)

