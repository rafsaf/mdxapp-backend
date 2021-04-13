from rest_framework import serializers
from .models import App


class SimpleAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["slug", "people", "updated_at"]