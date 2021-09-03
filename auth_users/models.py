from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token



class User(AbstractUser):
    @property
    def token(self):
        try:
            token = Token.objects.get(user=self)
            token.delete()
            token = Token.objects.create(user=self)
        except Token.DoesNotExist:
            token = Token.objects.create(user=self)
        return token.key