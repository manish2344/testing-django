# tests/test_forms.py
from django.test import TestCase
from globalapp.forms import MyForm

class MyFormTestCase(TestCase):
    def test_form_rendering(self):
        # Test form rendering
        form = MyForm()
        self.assertInHTML('<input type="text" name="name">', form.as_p())
        self.assertInHTML('<input type="number" name="value">', form.as_p())

    def test_form_submission_valid(self):
        # Test form submission with valid data
        form_data = {'name': 'Test Object', 'value': 10}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_submission_invalid(self):
        # Test form submission with invalid data
        form_data = {'name': '', 'value': 'abc'}  # Invalid data
        form = MyForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('value', form.errors)

    def test_custom_validation_method(self):
        # Test custom validation method
        form_data = {'name': 'Test Object', 'value': 5}  # Invalid value for custom validation
        form = MyForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('value', form.errors)
