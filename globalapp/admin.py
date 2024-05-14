from django.contrib import admin
from .models import Profile, Category, Product, Order, OrderItem, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Profile)
admin.site.register(Category, CategoryAdmin)  # Register CategoryAdmin instead of Category
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
