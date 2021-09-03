from rest_framework import serializers, validators
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


# Register serialaizer
class UserRegisterSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=64, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=200, write_only=True)
    password2 = serializers.CharField(max_length=200, write_only=True)

    def create(self, validated_data):
        username = validated_data.get("username", None)
        password = validated_data.get("password", None)
        password2 = validated_data.get("password2", None)

        if password != password2:
            raise validators.ValidationError({'message:parollar bir biriga mos emas!'})
        if User.objects.filter(username=username).count() > 0:
            raise validators.ValidationError({'message:bu username band!'})

        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


# Login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64,write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=200, read_only=True)

    def validate(self, attrs):
        username = attrs.get("username", None)
        password = attrs.get("password", None)

        user = authenticate(username=username, password=password)

        if user is None:
            raise validators.ValidationError({"message":"username yoki parol xato!"})

        return {
            # 'username':user.username,
            'token':user.token
        }