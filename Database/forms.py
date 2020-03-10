from django import forms
from .models import userInfo



dc = [('', 'Designation'),
    ('1', 'Country Head'),
    ('2', 'State Head'),
    ('3', 'City Head'),
    ('4', 'Employees')]
class suform(forms.Form):
    first = forms.CharField(max_length=200)
    last = forms.CharField(max_length=200)
    number = forms.IntegerField()
    designation = forms.Select(choices=dc)
    password = forms.PasswordInput()




