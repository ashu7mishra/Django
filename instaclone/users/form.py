from django import forms
from .models import User

class UserSignUpForm(forms.ModelForm):

    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={
                                   "placeholder": "Provide your full name",
                                   "class": "input-fields"
                               }
                           ), label="Full name")

    email = forms.EmailField(required=True)

    password = forms.CharField(required=True)

    class Meta:
        model = User
        exclude = ('created_on', 'updated_on', 'is_active')

