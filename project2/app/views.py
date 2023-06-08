from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class Productcurd(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductCS(PQS,many=True)
        return Response(PJD.data)
