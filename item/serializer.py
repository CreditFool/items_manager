from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item


class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all()
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'items', 'owner')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price', 'owner')
    
    def create(self, validated_data):
        return Item.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for field in fields(Item):
            if field.name in validated_data:
                setattr(instance, field.name, validated_data[field.name])
        instance.save()
        return instance