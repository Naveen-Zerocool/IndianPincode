from rest_framework import serializers
from .models import IndianPincode


class IndianPincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndianPincode
        fields = '__all__'
