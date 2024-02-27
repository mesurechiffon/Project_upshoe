from django.urls import path
from .views import My_shoesList, My_shoesDetail, review_list

urlpatterns = [
    path('my_shoes', My_shoesList.as_view()),
    path('my_shoes/<int:pk>', My_shoesDetail.as_view()),
    path('my_shoes/<int:pk>/reviews', review_list)
]