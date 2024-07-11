from rest_framework import serializers

from .models import Church, Cult


class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = '__all__'


class CultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cult
        fields = '__all__'


class ListCultChurchSerializer(serializers.ModelSerializer):
    church = serializers.ReadOnlyField(source='church.name')

    class Meta:
        model = Cult
        fields = ['church', 'date', 'preacher']
