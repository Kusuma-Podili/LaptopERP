from django import forms
from .models import LaptopModel, LaptopUnit, Brand, ComponentItem


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = LaptopModel
        fields = '__all__'
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.Select(attrs={'class': 'form-select'}),
            'ram': forms.Select(attrs={'class': 'form-select'}),
            'storage': forms.Select(attrs={'class': 'form-select'}),
            'display': forms.Select(attrs={'class': 'form-select'}),
            'gpu': forms.Select(attrs={'class': 'form-select'}),
            'msrp_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'standard_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LaptopUnitForm(forms.ModelForm):
    class Meta:
        model = LaptopUnit
        fields = ['laptop_model', 'serial_number', 'condition_grade', 'purchase_price', 'selling_price', 'current_location', 'notes']
        widgets = {
            'laptop_model': forms.Select(attrs={'class': 'form-select'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'condition_grade': forms.Select(attrs={'class': 'form-select'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_location': forms.TextInput(attrs={'class': 'form-control'}),
        }
