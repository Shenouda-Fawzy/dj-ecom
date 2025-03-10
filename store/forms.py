# Django forms https://docs.djangoproject.com/en/5.1/topics/forms/
# Django widget https://docs.djangoproject.com/en/5.1/ref/forms/widgets/

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreation(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100)
    user_email = forms.EmailField()


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput)
    first_name = forms.CharField(label="", max_length=100)
    last_name = forms.CharField(label="", max_length=100)

    class Meta:

        # This to define which model the Form will bind to in
        # this case this is the User model from Django auth system
        model = User

        # This to associate the form fields with the User model
        # this is also will specify the order of display
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        # Username styling
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # Password1 styling
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # Password2 styling
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        
