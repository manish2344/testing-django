# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_view_success(self):
        # Test a successful GET request to the view
        response = self.client.get(reverse('my-view'))
        self.assertEqual(response.status_code, 200)

    def test_my_view_not_found(self):
        # Test for a non-existent URL
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)

    def test_my_view_internal_server_error(self):
        # Test for an intentional internal server error in the view
        response = self.client.get(reverse('error-view'))
        self.assertEqual(response.status_code, 500)

    def test_my_view_bad_request(self):
        # Test for a POST request with invalid data
        data = {'invalid_field': 'Invalid Data'}
        response = self.client.post(reverse('my-view'), data)
        self.assertEqual(response.status_code, 400)

    def test_my_view_permission_denied(self):
        # Test for accessing a view that requires authentication
        response = self.client.get(reverse('secured-view'))
        self.assertEqual(response.status_code, 403)
