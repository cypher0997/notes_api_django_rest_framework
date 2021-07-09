from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError


class RegisterUserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_username(self, value):
        if User.objects.filter(username=value):
            return ValidationError("USER ALREADY EXIST, CAN NOT STORE THIS USER")
        return value
