from rest_framework import generics, viewsets, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import PostModel
from .serializers import PostSerializer

'''
class PostViewSet(viewsets.ModelViewSet):
#view
    def get(self, request, *args, **kwargs):
        queryset = PostModel.objects.all()
        serializer = PostSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
#create
        data = {
            'content_id': request.data.get('content_id'), 
            'content_title': request.data.get('content_title'), 
            'content': request.data.get('content'),
        }
        serializer = PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 '''   

class PostViewSet(viewsets.ModelViewSet):
   queryset = PostModel.objects.all()
   serializer_class = PostSerializer
