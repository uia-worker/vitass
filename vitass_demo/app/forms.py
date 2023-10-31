from django import forms
from .models import UploadedFile

# from martor.fields import MartorFormField
# from app.models import Post


class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    # description = MartorFormField()
    # wiki = MartorFormField()


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]


class SimpleTestForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())