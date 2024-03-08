from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from .models import My_shoes, Review
from .serializers import My_shoesSerializer, ReviewSerializer

class My_shoesList(ListCreateAPIView):
    queryset = My_shoes.objects.all()
    serializer_class = My_shoesSerializer

class My_shoesDetail(RetrieveUpdateDestroyAPIView):
    queryset = My_shoes.objects.all()
    serializer_class = My_shoesSerializer

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        my_shoes = get_object_or_404(My_shoes, pk=self.kwargs.get('pk'))
        return Review.objects.filter(my_shoes=my_shoes)
	
    def perform_create(self, serializer):
        my_shoes = get_object_or_404(My_shoes, pk=self.kwargs.get('pk'))
        serializer.save(my_shoes=my_shoes)