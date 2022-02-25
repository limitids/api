from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post
from API.serializers import PostSerializer

# Create your views here.


def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status =400)