from django.test import TestCase
# from .models import 
from globalapp.models import Category, Profile, Product, Order, OrderItem, Review
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword')

        self.category = Category.objects.create(
            name='Test Category', description='Test Description')

        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00, category=self.category)

        self.order = Order.objects.create(
            user=self.user, total_amount=20.00)

        self.order_item = OrderItem.objects.create(
            order=self.order, product=self.product, quantity=2, price=10.00)

        self.review = Review.objects.create(
            user=self.user, product=self.product, rating=5, comment='Great product!')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user, address='Test Address', phone_number='1234567890')
        self.assertEqual(profile.user.username, 'testuser')

    def test_product_manager(self):
        self.assertEqual(Product.objects.count(), 1)
        self.product.is_active = False
        self.product.save()
        self.assertEqual(Product.objects.count(), 0)

    def test_order_total_amount(self):
        self.assertEqual(self.order.total_amount, 20.00)

    def test_order_item_price(self):
        self.assertEqual(self.order_item.price, 10.00)

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 5)
