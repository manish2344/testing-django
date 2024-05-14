# forms.py
from django import forms
from globalapp.models import Category
from .models import Product

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter product name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Enter product description'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter product price'})
