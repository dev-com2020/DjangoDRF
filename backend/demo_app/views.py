from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def hello_world(request, *args, **kwargs):
    return HttpResponse('Witaj w Django!')


@api_view(['GET'])
def hello_world_drf(request, *args, **kwargs):
    return Response(data={'msg': 'Witaj w Django!'})
