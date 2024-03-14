from django import forms

from pets.models import ClientProfile


class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['client_name', 'client_bio', 'profile_image']
