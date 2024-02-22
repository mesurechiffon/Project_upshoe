from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import My_shoes
from .serializers import My_shoesSerializer

@api_view(['GET', 'POST'])
def my_shoes_list(request):
    if request.method == 'GET':
        my_shoes = My_shoes.objects.all()
        serializer = My_shoesSerializer(my_shoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = My_shoesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def my_shoes_detail(request, pk):
    my_shoes = get_object_or_404(My_shoes, pk=pk)
    if request.method == 'GET':
        serializer = My_shoesSerializer(my_shoes)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = My_shoesSerializer(my_shoes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        my_shoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)