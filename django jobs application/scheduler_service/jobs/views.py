from rest_framework import generics
from .models import Job
from .serializers import JobSerializer


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    git
# jobs/views.py
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

class JobDetailView(APIView):
    def get(self, request, id, format=None):
        job = get_object_or_404(Job, id=id)
        serializer = JobSerializer(job)
        return Response(serializer.data)
