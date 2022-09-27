from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from phone_auth.models import PhoneNumber, EmailAddress


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2",
                  "first_name", "last_name", "phone")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
            EmailAddress(email=user.email, is_verified=False, user=user).save()
            PhoneNumber(phone=user.phone, is_verified=False, user=user).save()
        return user
