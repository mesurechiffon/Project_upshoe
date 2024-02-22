from rest_framework import serializers
from .models import My_shoes

class My_shoesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=100)
    model_name = serializers.CharField(max_length=100)
    model_num = serializers.CharField(max_length=50)
    release_date = serializers.DateField()
    release_price = serializers.IntegerField()
    purchase_date = serializers.DateField()
    purchase_price = serializers.IntegerField()

    def create(self, validated_data):
        return My_shoes.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.model_num = validated_data.get('model_num', instance.model_num)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.release_price = validated_data.get('release_price', instance.release_price)
        instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
        instance.purchase_price = validated_data.get('purchase_price', instance.purchase_price)
        instance.save()
        return instance