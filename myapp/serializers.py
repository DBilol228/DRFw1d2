from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['country'] = CountrySerializer(instance.country).data
        return data

class BookSerializer(serializers.ModelSerializer):
    title_upper = serializers.SerializerMethodField()
    is_expensive = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id','title','pages','price','author','title_upper','is_expensive']
    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError('Title must start with a capital letter')
        return value
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value
    def validate(self,data):
        if data['pages'] > 1000 and data['price'] < 200:
            raise serializers.ValidationError('If pages > 1000, price must be at least 200')
        return data
    def get_title_upper(self,obj):
        return obj.title.upper()
    def get_is_expensive(self,obj):
        return obj.price > 200
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = AuthorSerializer(instance.author).data
        data['book_info'] = f'{instance.title} - {instance.pages} pages'
        return data