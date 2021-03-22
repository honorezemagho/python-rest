from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializers):
    class Meta:
        model = Customer
        fields = [
            'id', 'address', 'profession', 'datasheet'
            ]