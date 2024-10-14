from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kittens.views import BreedViewSet, KittenViewSet


router = DefaultRouter()
router.register(r'breeds', BreedViewSet)
router.register(r'kittens', KittenViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
