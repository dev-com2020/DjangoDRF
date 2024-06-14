from cacheops import cached
from rest_framework import views, response, status, generics, filters

from blog import models
from blog import serializers

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from backend.common.logging_util import log_event, log_error


class BlogGetCreateView(views.APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_scope = 'blog'

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

    def delete(self, request, pk):
        try:
            blog = models.Blog.objects.get(pk=pk)
        except models.Blog.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class BlogGetUpdateView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        blogs_queryset = models.Blog.objects.filter(id__gt=1)
        return blogs_queryset


class BlogGetUpdateFilterView(generics.ListAPIView):
    serializer_class = serializers.BlogSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']


class BlogGetUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


@cached(timeout=60 * 10)
def get_all_blogs(author_id=1):
    print('Pobieram wszystkie wpisy autora')
    blogs = models.Blog.objects.filter(author_id=author_id)
    blogs_data = serializers.BlogSerializer(blogs, many=True).data
    return blogs_data


@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(['GET'])
def get_blogs_by_author(request):
    author_id = request.GET.get('author_id')
    if author_id is not None:
        try:
            author_id = int(author_id)
            log_event('get_blogs_by_author', {'author_id': author_id})
        except ValueError:
            log_error('error', {'author_id': author_id})
            return Response({'error': 'Niepoprawny id autora'}, status=status.HTTP_400_BAD_REQUEST)

        blogs = get_all_blogs(author_id)
        return Response({'blogs': blogs})
    else:
        return Response({'error': 'podanie id autora jest wymagane'}, status=status.HTTP_400_BAD_REQUEST)
