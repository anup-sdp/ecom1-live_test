# accounts, authentication.py:
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        OurUser = get_user_model()
        try:
            user = OurUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except OurUser.DoesNotExist:
            return
