from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'comment', 'name', 'email')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'category')

class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'category', 'comments')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('url', 'title')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
