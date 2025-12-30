from django import forms

from .models import MessageModel


class FormModelMessage(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = [
            "message",
        ]
