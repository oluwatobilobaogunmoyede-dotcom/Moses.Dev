from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "How can I help?",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Tell me about your project...",
                "rows": 6,
            }),
        }
