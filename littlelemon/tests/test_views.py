from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# class MenuViewTest(TestCase):
#     def test_getall(self):
#         items = setup(self)

#         response = self.client.get('/restaurant/menu/')
#         self.assertEquals(response.status_code, 200)
#         self.assertQuerysetEqual(
#             response.data,
#             items.data
#         )

class MenuViewTest(TestCase):   
    def setup(self):
        item1 = Menu.objects.create(title="Peanuts", price=1.99, inventory=2)
        item2 = Menu.objects.create(title="Cake", price=5.99, inventory=3)
        items = Menu.objects.all()

        return MenuSerializer(items, many=True)

    def test_getall_unauth(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        self.assertEquals(response.status_code, 401)
    
    def test_getall_auth(self):
        client = APIClient()
        client.force_login(User.objects.get_or_create(username='testuser')[0]) 
        items = self.setup()
        response = client.get('/restaurant/menu/')
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.data,
            items.data
        )
        client.logout()

    
