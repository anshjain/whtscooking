from django import forms


EMP_USER = 'emp'
VDOR_USER = 'vdor'
USER_TYPES = [
    (EMP_USER, 'Employee'),
    (VDOR_USER, 'vendor')
]


class LoginForm(forms.Form):
    """ login form """
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect(), initial=EMP_USER)
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'password'}))
