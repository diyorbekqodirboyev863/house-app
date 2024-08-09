from django import forms
from .models import House, Image

class HouseForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}), required=True)

    class Meta:
        model = House
        fields = ['title', 'description', 'price', 'house_type', 'location', 'location_URL', 'bedrooms', 'bathrooms', 'square_feet', 'posted_by', 'posted_on', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}),
            'location_URL': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location URL'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bedrooms'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bathrooms'}),
            'square_feet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Square Feet'}),
            'posted_by': forms.Select(attrs={'class': 'form-control'}),
            'posted_on': forms.HiddenInput(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        images = self.files.getlist('images')
        for image in images:
            Image.objects.create(house=instance, image=image)
        return instance
