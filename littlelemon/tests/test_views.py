from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse

class MenuViewTest(TestCase):   
    def setup(self):
        item1 = Menu.objects.create(title="Peanuts", price=1.99, inventory=2)
        item2 = Menu.objects.create(title="Cake", price=5.99, inventory=3)
        items = Menu.objects.all()
        
        return items
    
    def setup_single(self):
        item = Menu.objects.create(title="Peanuts", price=1.99, inventory=2)
        return item

    def test_getall_unauth(self):
        client = APIClient()
        response = client.get(reverse('MenuItemsView'))
        self.assertEquals(response.status_code, 401)
    
    def test_getall_auth(self):
        client = APIClient()
        client.force_login(User.objects.get_or_create(username='testuser')[0]) 
        items = self.setup()
        response = client.get(reverse('MenuItemsView'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.data,
            MenuSerializer(items, many=True).data
        )
        client.logout()
    
    def test_getsingle_auth(self):
        client = APIClient()
        client.force_login(User.objects.get_or_create(username='testuser')[0]) 
        item = self.setup_single()
        response = client.get(reverse('SingleMenuItemView', args=[item.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.data,
            MenuSerializer(item).data
        )
        client.logout()
        

    
