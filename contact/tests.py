import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Contact
from .serializers import ContactSerializer


# create your test here.

class ContactTestCase(APITestCase):
    
    def test_contact(self):
        data = {"name": "Moe Jallow", "email": "jallowmo@gmail.com", "message": "hello"}
        response = self.client.post("/contact", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)