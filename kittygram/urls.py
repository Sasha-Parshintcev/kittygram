from django.urls import path, include

from cats.views import CatViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet, basename='tiger')

urlpatterns = [
    path('', include(router.urls)),
] 
