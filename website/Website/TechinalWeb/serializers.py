from rest_framework import serializers
from .models import students

class studentserializer(serializers.ModelSerializer):

    class Meta:
        model=students
        # fields=('firstname','lastname')
        fields = '__all__'