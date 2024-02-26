from rest_framework import serializers
from .models import My_shoes, Review

class My_shoesSerializer(serializers.ModelSerializer):
    my_shoes_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    
    class Meta:
        model = My_shoes
        fields = ['id', 'brand', 'model_name', 'model_num', 'release_date', 'release_price', 'purchase_date', 'purchase_price', 'my_shoes_reviews']


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

class ReviewSerializer(serializers.ModelSerializer):
    my_shoes = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id', 'my_shoes', 'username', 'star', 'comment', 'created']