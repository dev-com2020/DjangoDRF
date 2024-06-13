from rest_framework import serializers

from blog import models


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'
        extra_kwargs = {
            'title': {'min_length': 1, 'required': True},
            'updated_at': {'write_only': True}
        }
