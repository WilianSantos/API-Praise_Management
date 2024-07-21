from rest_framework import serializers

from .models import Church, Cult, Function, Member


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
        fields = ['church', 'date', 'preacher', 'theme']


class FunctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
