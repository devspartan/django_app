from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=40, label="Product Title")
    desc = forms.CharField()
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    summary = forms.CharField(required=False)

    class Meta:
        model = Products
        fields = ['title', 'price', 'desc',"summary", 'check', 'mail', 'dt']


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "dev" not in title:
            raise forms.ValidationError("Not a valid Username")
        return title

class RawForm(forms.Form):
    title = forms.CharField(max_length=40, label="Product Title")
    desc = forms.CharField()
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    summary = forms.CharField(required=False)