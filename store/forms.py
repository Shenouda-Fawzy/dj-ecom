# Django forms https://docs.djangoproject.com/en/5.1/topics/forms/
# Django widget https://docs.djangoproject.com/en/5.1/ref/forms/widgets/

from django import forms


class UserCreation(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100)
    user_email = forms.EmailField()
