from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class AuthenticateUser(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticateUser, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
