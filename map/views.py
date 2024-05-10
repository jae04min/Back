from django.shortcuts import render
from django.http import JsonResponse
from .models import Hospital, Snippet
from rest_framework.decorators import  api_view
from .serializers import HospitalSerializer, SnippetSerializer

@api_view(['GET'])
def hospital_list(request):
    snippet = Snippet(code='test')
    print(snippet.code)
    # hospitals = Hospital.objects.all()
    # serializer = HospitalSerializer(hospitals, many=True)
    serializer = SnippetSerializer(snippet)
    
    return JsonResponse(serializer.data, safe=False)
