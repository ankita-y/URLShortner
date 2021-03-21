from rest_framework.serializers import ModelSerializer
from .models import URLLink

class URLSerializer(ModelSerializer):
    class Meta:
        model = URLLink
        fields='__all__'