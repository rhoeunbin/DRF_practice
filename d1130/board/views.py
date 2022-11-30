from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Board
from .serializers import BoardSerializer
from rest_framework import status


### FBV api_view decorator
@api_view(['GET','POST'])
def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    else:
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)