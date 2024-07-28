from django import forms


class ChatForm(forms.Form):
    msg = forms.CharField(max_length=50)