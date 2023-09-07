from rest_framework import serializers
from .models import notebooks, Bolalar


class notebooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=notebooks
        fields = ('name', 'count')


class bolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolalar
        fields=('name', 'number')



