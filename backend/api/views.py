
from re import sub
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from backend.api.serializers import *
from backend.models import *
from user_app.api.permissions import IsCurrentUserOrAdmin



class LessonOrderView(generics.ListCreateAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = LessonOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return LessonOrder.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class DocumentOrderView(generics.ListCreateAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return DocumentOrder.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class DocumentView(generics.ListCreateAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentSerializer

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)
