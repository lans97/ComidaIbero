from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .iberoApi import ibero_auth  # Import your API authentication function

User = get_user_model()

class IberoAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the user is registered locally
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If not registered locally, ask the API for authentication
            api_user = ibero_auth(username, password)
            if api_user:
                # If API authentication is successful, create a local user
                user = User.objects.create_user(username=api_user['username'])
                user.password = make_password(password)
                user.save()
            else:
                return None  # API authentication failed, return None

        # Check local authentication
        if user.check_password(password):
            return user  # Local authentication successful
        else:
            return None  # Local authentication failed
