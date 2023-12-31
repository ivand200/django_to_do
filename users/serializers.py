from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "username")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)