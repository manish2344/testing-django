from django.test import TestCase, Client
from django.urls import reverse
# from .models import Product, OrderItem, Order, Category, Review
from globalapp.models import Product, OrderItem, Order, Category, Review
from django.contrib.auth.models import User
# from .forms import ProductForm
from globalapp.forms import ProductForm
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword')
        self.category = Category.objects.create(
            name='Test Category', description='Test Description')
        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00, category=self.category)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # Add similar test methods for other views...

    def test_add_product_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_product'), {'name': 'New Product', 'description': 'New Description', 'price': 20.00, 'category': self.category.id})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    # def test_product_list_view(self):
    #     response = self.client.get(reverse('product_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'product_list.html')
    #     self.assertQuerysetEqual(response.context['products'], ['<Product: Test Product>'])
def test_product_list_view(self):
    # Access the view
    response = self.client.get(reverse('product_list'))

    # Check the status code
    self.assertEqual(response.status_code, 200)

    # Check if products are present in the context
    self.assertIn('products', response.context)

    # Get the queryset from the response context
    products_queryset = response.context['products']

    # Print the queryset for debugging
    print("Products queryset:", products_queryset)

    # Check if the queryset is not empty
    self.assertTrue(products_queryset.exists())

    # Compare the product names in the queryset with the expected names
    expected_product_names = ['Test Product']
    actual_product_names = [str(product) for product in products_queryset]
    self.assertListEqual(actual_product_names, expected_product_names)

    def test_add_to_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(OrderItem.objects.filter(product=self.product).exists())

    # Add similar test methods for other views...
