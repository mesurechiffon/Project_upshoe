from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import My_shoes, Review
from .serializers import My_shoesSerializer, ReviewSerializer

class My_shoesList(APIView):
    def get(self, request):
        my_shoes = My_shoes.objects.all()
        serializer = My_shoesSerializer(my_shoes, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = My_shoesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class My_shoesDetail(APIView):
    def get_object(self, pk):
        my_shoes = get_object_or_404(My_shoes, pk=pk)
        return my_shoes
    
    def get(self, request, pk):
        my_shoes = self.get_object(pk)
        serializer = My_shoesSerializer(my_shoes)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        my_shoes = self.get_object(pk)
        serializer = My_shoesSerializer(my_shoes, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        my_shoes = self.get_object(pk)
        my_shoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'POST'])
def review_list(request, pk):
    my_shoes = get_object_or_404(My_shoes, pk=pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(my_shoes=my_shoes)
        serialzer = ReviewSerializer(reviews, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(my_shoes=my_shoes)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
