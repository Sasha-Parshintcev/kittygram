from django.urls import path

from cats.views import api_posts_detail, cat_list

urlpatterns = [
   path('cats/', cat_list),
   path('api/v1/posts/<int:pk>/', api_posts_detail),
]
