from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

widgets_textarea = forms.Textarea(
    attrs={
        "class": "form-control",
    }
)
widgets_textinput = forms.TextInput(
    attrs={
        "class": "form-control",
    }
)

class TextForm(forms.Form):
    text = forms.CharField(label="", widget=widgets_textarea)
    search = forms.CharField(label="検索", widget=widgets_textinput)
    replace = forms.CharField(label="置換", widget=widgets_textinput)




