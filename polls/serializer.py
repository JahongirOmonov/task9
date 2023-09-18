from rest_framework import serializers
from .models import notebooks, Bolalar
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


class notebooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=notebooks
        fields = ('__all__')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(notebooksSerializer, self).create(validated_data)



class bolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolalar
        fields=('__all__')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(bolalarSerializer, self).create(validated_data)





