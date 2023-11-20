from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .iberoApi import ibero_auth

User = get_user_model()

class IberoAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            api_user = ibero_auth(username, password)
            if api_user:
                user = User.objects.create_user(username=api_user['username'])
                user.password = make_password(password)
                user.save()
            else:
                return None

        if user.check_password(password):
            return user
        else:
            return None
