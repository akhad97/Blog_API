from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters import rest_framework as filter
from rest_framework import filters


class PostFilter(filter.FilterSet):
    class Meta:
        model = Post
        fields ={'title': ['icontains']}


class PostViewSet(viewsets.ModelViewSet):
    # http_method_names = ['post']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return self.serializer_class


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class CategoryFilter(filter.FilterSet):
    class Meta:
        model = Category
        fields ={'name': ['icontains']}


class CommentViewSet(viewsets.ModelViewSet):
    # http_method_names = 'post'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # lookup_field = 'name'

class ContactViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



