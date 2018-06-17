from rest_framework import serializers

from finance.models import HelloWorldEntity


class HelloWorldEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloWorldEntity
        fields = ('id', 'name', 'array_field', 'integer_range_field', 'json_field')
