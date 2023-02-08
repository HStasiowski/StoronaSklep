from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_unicode_slug


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Imię", min_length=2, max_length=30, validators=[validate_unicode_slug])
    last_name = forms.CharField(label="Nazwisko", min_length=2, max_length=30, validators=[validate_unicode_slug])
    user_email = forms.EmailField(label="Email", max_length=75, validators=[validate_email])
    username = forms.CharField(label="Nazwa użytkownika", max_length=30, validators=[validate_unicode_slug])
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(), validators=[validate_password])
    confirm_password = forms.CharField(label="Potwierdzenie hasła", widget=forms.PasswordInput(), )
    captcha = ReCaptchaField(label="Captcha", widget=ReCaptchaV2Checkbox)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check emails are identical
        if password != confirm_password:
            err_msg = ValidationError("Passwords must be identical")
            self.add_error("password", err_msg)
            self.add_error("confirm_password", err_msg)
