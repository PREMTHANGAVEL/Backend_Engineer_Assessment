from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name', 'schedule_interval', 'last_run_time', 'next_run_time'] #'created_at', 'updated_at


# jobs/serializers.py

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'  # or specify the fields you want to include
