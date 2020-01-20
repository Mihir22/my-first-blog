from django import forms
from dbase.models import user

class user_info(forms.ModelForm):
    class Meta():
        model = user
        fields = '__all__'
