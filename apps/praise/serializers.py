from rest_framework import serializers

from .models import Cast


class CastSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'
