from django.shortcuts import render
from leads.serializers import LeadSerializer
from leads.models import Lead
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
	queryset=Lead.objects.all()
	serializer_class=LeadSerializer


# Create your views here.
