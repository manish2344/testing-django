from django.test import TestCase
# from .forms import ProductForm
from globalapp.forms import ProductForm
from globalapp.models import Category

class TestForms(TestCase):

    def test_product_form_valid_data(self):
        category = Category.objects.create(name='Test Category', description='Test Description')
        form = ProductForm(data={'name': 'Test Product', 'description': 'Test Description', 'price': 10.00, 'category': category.id})
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  # 4 fields in the form

    def test_product_form_field_attributes(self):
        form = ProductForm()
        self.assertEqual(form.fields['name'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['name'].widget.attrs['placeholder'], 'Enter product name')
        # Add similar assertions for other fields...
