from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase): 
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(f'{item.title}: {str(item.price)}', "IceCream: 80")