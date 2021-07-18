from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Table
# Create your tests here.

class TestTable(APITestCase):
    url = "/table"
    
    def setUp(self):
        Table.objects.create(name)