from django.urls import path
from djshop.apps.catalog.views.front import Category_CB
# from rest_framework.routers import SimpleRouter
#
# from src.djshop.apps.catalog.views.front import CategoryViewSet
#
# router = SimpleRouter()
# router.register(prefix='categories', viewset=CategoryViewSet)

urlpatterns = [
    path('test', Category_CB.as_view()),
]
