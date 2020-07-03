from django import forms


class LoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
        )


class RegisterForm(forms.Form):
    '''
    Form used to create and register new user
    '''
    # First name
    first_name = forms.CharField(
        max_length=20,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    # Last name
    last_name = forms.CharField(
        max_length=20,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    # username
    username = forms.CharField(
        max_length=20,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    # Email
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    # First password entry
    password = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    # Password confrim entry
    password_confirm = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
