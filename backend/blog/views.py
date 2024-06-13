from cacheops import cached
from rest_framework import views, response, status, generics, filters

from blog import models
from blog import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response


class BlogGetCreateView(views.APIView):


    def get(self, request):
        blogs_obj_list = models.Blog.objects.all()
        blogs = serializers.BlogSerializer(blogs_obj_list, many=True)
        return response.Response(blogs.data)

    def post(self, request):
        input_data = request.data
        b_obj = serializers.BlogSerializer(data=input_data)
        if b_obj.is_valid():
            b_obj.save()
            return response.Response(b_obj.data, status=status.HTTP_201_CREATED)
        return response.Response(b_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogGetUpdateView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        blogs_queryset = models.Blog.objects.filter(id__gt=1)
        return blogs_queryset


class BlogGetUpdateFilterView(generics.ListAPIView):
    serializer_class = serializers.BlogSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']


@cached(timeout=60 * 10)
def get_all_blogs(author_id=1):
    print('Pobieram wszystkie wpisy autora')
    blogs = models.Blog.objects.filter(author_id=author_id)
    blogs_data = serializers.BlogSerializer(blogs, many=True).data
    return blogs_data


@api_view(['GET'])
def get_blogs_by_author(request):
    author_id = request.GET.get('author_id')
    blogs = get_all_blogs(author_id)
    return Response({'blogs': blogs})
