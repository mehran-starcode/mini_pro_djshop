from django.urls import path
from djshop.apps.catalog.views.front import Category_CB, category

# from rest_framework.routers import SimpleRouter
#
# from src.djshop.apps.catalog.views.front import CategoryViewSet
#
# router = SimpleRouter()
# router.register(prefix='categories', viewset=CategoryViewSet)

urlpatterns = [
    path('simple-classbase-view', Category_CB.as_view()),
    path('funcbase-view', category, {}),
]
