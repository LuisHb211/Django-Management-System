from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    # This class is goig to earn all the atr from the Product class in models.py
    model = Product
    fields = '__all__'
    labels = {
      'product_id':'Product ID',
      'name':'Name',
      'sku':'SKU',
      'price':'Price',
      'quantity':'Quantity',
      'supplier':'Supplier'
      }
    # Specify the type of input widget to render it field of the form
    widgets = {
      'product_id':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
      'name':forms.TextInput(attrs={'placeholder':'e.g shirt', 'class':'form-control'}),
      'sku':forms.TextInput(attrs={'placeholder':'e.g S1234', 'class':'form-control'}),
      'price':forms.NumberInput(attrs={'placeholder':'e.g 19.99', 'class':'form-control'}),
      'quantity':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
      'supplier':forms.TextInput(attrs={'placeholder':'e.g ABC Corp', 'class':'form-control'}),
      
    }
    