from rest_framework import serializers
from .models import *

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'