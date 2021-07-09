from django.contrib.auth import authenticate
import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialize import RegisterUserSer
from django.core.exceptions import ValidationError


class LoginView(APIView):
    def post(self, request):
        try:
            data = User.objects.all()
            print(data)
            if data.filter(username=request.data.get("username")).filter(password=request.data.get("password")):
                return Response({"message": "USER LOGGED IN"}, status=200)
            return Response({"message": "USER NOT FOUND"}, status=400)
        except Exception as e:
            return Response(e)


class RegisterView(APIView):
    def post(self, request):
        try:
            new_usr = User(username=request.data.get("username"), first_name=request.data.get("first_name"),
                           email=request.data.get("email"), password=request.data.get("password"))
            ser = RegisterUserSer(new_usr)
            neo_ser = RegisterUserSer(data=ser.data)
            if neo_ser.is_valid():
                neo_ser.save()
                return Response({"message": "USER CREATED"}, status=200)
            return Response({"message": "USER CAN NOT BE CREATED"}, status=400)
        except ValidationError as e:
            return Response(e.message)
