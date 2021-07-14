from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError


class RegisterUserSer(serializers.ModelSerializer):
    # it is class which serialize the data
    class Meta:
        model = User
        fields = "__all__"

    def validate_username(self, value):
        """
        this method validates the deserialized data
        :param value: username that is to be validated
        :return: returns username for further operations
        """
        if User.objects.filter(username=value):
            return ValidationError("USER ALREADY EXIST, CAN NOT STORE THIS USER")
        return value
