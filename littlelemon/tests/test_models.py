from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuItemTest(TestCase): 
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(f'{item.title}: {str(item.price)}', "IceCream: 80")

class BookingTest(TestCase):
    def test_get_booking(self):
        booking1 = Booking.objects.create(name="BDay Dinner", no_of_guests=3, bookingdate="2023-02-07T14:38:19Z")
        self.assertEqual(f'{booking1.bookingdate}: {booking1.name}', "2023-02-07T14:38:19Z: BDay Dinner")