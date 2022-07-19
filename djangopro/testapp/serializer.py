from rest_framework import serializers
from .models import Employee

class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with r")
# class EmployeeSer(serializers.Serializer):
#     ename = serializers.CharField(max_length=64,validators=[start_with_r])
#     eno = serializers.IntegerField()
#     esal = serializers.FloatField()
#     eaddr = serializers.CharField(max_length=64)
#
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eaddr = validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance
#
#     def validate_esal(self, value):
#         if value <= 5000:
#             raise serializers.ValidationError("Salary should be more than 5000")
#         return value
#     def validate(self,data):
#         name=data.get('ename')
#         addr=data.get('eaddr')
#         if name.lower() == "samrajyam" and addr.lower()!="chirala" :
#             raise serializers.ValidationError("City must be chirala")
#         return data