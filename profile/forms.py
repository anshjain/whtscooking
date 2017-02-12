from django import forms


EMP_USER = 'emp'
VDOR_USER = 'vdor'
USER_TYPES = [
    (EMP_USER, 'Employee'),
    (VDOR_USER, 'vendor')
]


class LoginForm(forms.Form):
    """ login form """
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect())
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)