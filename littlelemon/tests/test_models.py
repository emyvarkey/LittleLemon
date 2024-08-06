from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Mango Kulfi", price=10, inventory=100)
        self.assertEqual(str(item), "Mango Kulfi : 10.00")