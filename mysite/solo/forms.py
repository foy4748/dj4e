from django import forms

class MyForm(forms.Form):
    field1 = forms.CharField(label="Field 1")
    field2 = forms.CharField(label="Field 2")
