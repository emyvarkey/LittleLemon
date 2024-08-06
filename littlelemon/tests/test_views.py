from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.items = [
            Menu.objects.create(title="Kaju Kattli", price=14.40, inventory=80),
            Menu.objects.create(title="Veg Fried Rice", price=17.40, inventory=40),
            Menu.objects.create(title="Gobi Manchurian", price=16.23, inventory=40)
            ]

    def test_getall(self):
        expected_strings = [
            "Kaju Kattli : 14.40",
            "Veg Fried Rice : 17.40",
            "Gobi Manchurian : 16.23"
        ]
        for item, expected in zip(self.items, expected_strings):
            self.assertEqual(str(item), expected)