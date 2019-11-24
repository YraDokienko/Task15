from django.forms import ModelForm
from django import forms
from .models import Pizza


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'price', 'size', 'description', 'available', 'ingredient']


class PizzaPriceUpdateForm(forms.Form):
    value = forms.DecimalField(max_digits=7, decimal_places=2)

    def create_object(self):
        Pizza.objects.create(
            value=self.cleaned_data.get('value'),
        )
