
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
from django.shortcuts import get_object_or_404



class LessonOrderView(generics.ListCreateAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = LessonOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return LessonOrder.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class LessonOrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentOrderSerializer
    queryset = DocumentOrder.objects.all()

    def delete(self,request,pk):
        lesson_order = get_object_or_404(LessonOrder,pk=pk)
        order = lesson_order.order
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentOrderView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return DocumentOrder.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class DocumentOrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentOrderSerializer
    queryset = DocumentOrder.objects.all()

    def delete(self,request,pk):
        document_order = get_object_or_404(DocumentOrder,pk=pk)
        order = document_order.order
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentView(generics.ListCreateAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentSerializer

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class FormationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FormationSerializer

    queryset = Formation.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FormationSerializer(queryset, many=True)
        return Response(serializer.data)