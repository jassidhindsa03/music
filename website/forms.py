from django import forms
from .models import Album, Contact


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = "__all__"


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
