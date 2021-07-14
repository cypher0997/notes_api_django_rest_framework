from email.mime.text import MIMEText

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialize import RegisterUserSer
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from . import utils


class LoginView(APIView):
    # class representing view for user registration
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        """
        this method is used to register user or save user in database
        :param request: http request to made to this api
        :return: it returns response to request that is made:
        """
        try:
            user = User.objects.all()
            print(user)
            if user.filter(username=request.GET.get("username")).filter(password=request.GET.get("password")):
                return Response({"message": "USER LOGGED IN"}, status=200)
            print(request.user)
            return Response({"message": "USER LOGGED IN"}, status=200)
        except ObjectDoesNotExist as e:
            return Response(e)


class RegisterView(APIView):
    # class representing view for user login

    def post(self, request):
        """
       this method login user to system
        :param request: http request to made to this api
        :return: it returns response to request that is made:
        """
        try:
            new_usr = User(username=request.data.get("username"), first_name=request.data.get("first_name"),
                           email=request.data.get("email"), password=request.data.get("password"))
            serializer = RegisterUserSer(new_usr)
            deserialized_data = RegisterUserSer(data=serializer.data)
            if deserialized_data.is_valid():
                deserialized_data.save()
            key = "secret"
            token = jwt.encode({"username": request.data.get("username")}, key,
                               algorithm="HS256")
            print(token)
            utils.send_email(token)
            return Response({"message": "VERIFY YOURSELF, CHECK EMAIL"}, status=200)
        except ValidationError as e:
            return Response(e.message)


class VerifyView(APIView):
    # this class contain method for verification of user

    def get(self, request, token):
        """
        this method does the verification and confirmation if user successfully registered or not
        :param request: the request body
        :param token: token that contains credentials of user
        :return: returns corresponding response to users request
        """
        try:
            print(token)
            encoded = token
            key = "secret"
            usr_details = jwt.decode(encoded, key=key, algorithms="HS256")
            usr_name = usr_details.get("username")
            if User.objects.filter(username=usr_name):
                return Response({"message": "VERIFIED"}, status=200)
            return Response({"message": "SOME THING WENT WRONG"}, status=400)
        except Exception as e:
            return Response({"message": "SOMETHING WENT WRONG",
                             "detail": e.args}, status=400)
