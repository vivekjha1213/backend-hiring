from rest_framework import serializers
from website.models import Site

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class TaskSerializer(serializers.Serializer):
    job_type = serializers.IntegerField(min_value=1, max_value=5)
