from django import forms
from django.core import validators


class form_name(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail =  forms.EmailField(label = "Enter your email again: ")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,widget = forms.HiddenInput,validators = [validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']

        if email!=vmail:
            raise forms.ValidationError("Email does not match")
