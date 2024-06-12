from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def hello_world(request, *args, **kwargs):
    return HttpResponse('Witaj w Django!')


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def hello_world_drf(request, *args, **kwargs):
    if request.method == 'POST':
        return Response(data={'msg': 'Witaj metodzie POST!'})
    elif request.method == "PUT":
        return Response(data={'msg': 'Witaj metodzie PUT!'})
    elif request.method == "DELETE":
        return Response(data={'msg': 'Witaj metodzie DELETE!'})
    return Response(data={'msg': 'Witaj metodzie GET!'})

class DemoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'msg': 'Witaj metodzie GET!'})

    def post(self, request, *args, **kwargs):
        return Response(data={'msg': 'Witaj metodzie POST!'})

    def delete(self, request, *args, **kwargs):
        return Response(data={'msg': 'Witaj metodzie DELETE!'})

    def put(self, request, *args, **kwargs):
        return Response(data={'msg': 'Witaj metodzie PUT!'})
