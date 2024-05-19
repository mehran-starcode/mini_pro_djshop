from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from djshop.apps.catalog.models import Category
# from rest_framework import viewsets
# from djshop.apps.catalog.serializers.front import CategorySerializer


# class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class Category_CB(View):

    def get(self, request):
        return HttpResponse("Simple Class Base View Result")


def category(request):
    return HttpResponse('This Result is from Func Base View')
