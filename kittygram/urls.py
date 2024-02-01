from django.urls import path, include

from cats.views import CatViewSet, OwnerViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
