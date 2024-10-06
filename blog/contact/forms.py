from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'email': forms.EmailInput(attrs={'placeholder': ' Email Address '}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesaj '}),
        }
