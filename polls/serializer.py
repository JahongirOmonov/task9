from rest_framework import serializers
from .models import notebooks, Bolalar


class notebooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=notebooks
        fields = ('__all__')



class bolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolalar
        fields=('__all__')





