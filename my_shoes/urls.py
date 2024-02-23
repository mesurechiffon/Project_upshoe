from django.urls import path
from .views import my_shoes_list, my_shoes_detail, review_list

urlpatterns = [
    path('my_shoes', my_shoes_list),
    path('my_shoes/<int:pk>', my_shoes_detail),
    path('my_shoes/<int:pk>/reviews', review_list)
]