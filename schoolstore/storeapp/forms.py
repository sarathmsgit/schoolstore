from django import forms
from .models import UserDetails


class UserDetailsForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = UserDetails
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),

        }
