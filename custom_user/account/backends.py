from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.db.models import Q

class UsernameOrEmailOrMobileBackend(BaseBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        print("Yoyo")
        try:
            user = User.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            print(user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        print("Here = ",user_id)
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

        