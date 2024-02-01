from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('api/v1/cats/<int:pk>/', CatDetail.as_view()),
]
