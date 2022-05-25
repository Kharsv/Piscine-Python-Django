
from django import forms


class Login(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)

class Registration(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    password_check = forms.CharField(label='Check password', max_length=32, widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password_check")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class For_tip(forms.Form):
    text = forms.CharField(label="Text", max_length=1000)