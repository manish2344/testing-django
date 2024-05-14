# tests/test_models.py
from django.test import TestCase
from globalapp.models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='Test Object', value=10)

    def test_custom_method(self):
        # Test the custom method returns the expected value
        self.assertEqual(self.obj.custom_method(), 20)

    def test_custom_property(self):
        # Test the custom property returns the expected value
        self.assertEqual(self.obj.custom_property, 'Test Object Value: 10')

    def test_custom_property_setter(self):
        # Test setting the custom property updates the value correctly
        self.obj.custom_property = 'New Value'
        self.assertEqual(self.obj.value, 11)  # Assuming custom_property setter increments value by 1
