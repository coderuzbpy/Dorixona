from django import forms
from .models import Dori


class DoriForm(forms.ModelForm):
    class Meta:
        model = Dori
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Ismingizni togri kiriting")
        return name





