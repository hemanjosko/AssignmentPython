from django import forms
from .models import Router

class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = "sapid","hostname","loopback","macaddress"