from django import forms


class FileForm(forms.Form):
    file = forms.FileField()
    amount = forms.FloatField(label='Amount', required=False)
