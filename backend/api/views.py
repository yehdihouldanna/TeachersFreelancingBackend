
from re import sub
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from user_app.api.permissions import IsCurrentUserOrAdmin,IsTeacher
from backend.api.serializers import *
from backend.api.pagination import *
from backend.models import *

from django.shortcuts import get_object_or_404




class BookOrdersStudentHistoricView(generics.ListAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = BookOrderSerializer
    queryset = BookOrder.objects.all()

    def get(self,request,pk,*args,**kwargs):
        student = User.objects.get(pk=pk)
        orders = BookOrder.objects.filter(order__user=student)
        serializer = BookOrderSerializer(orders,many=True)
        return Response(serializer.data)

class LessonOrdersStudentHistoricView(generics.ListAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = LessonOrderSerializer
    queryset = LessonOrder.objects.all()

    def get(self,request,pk,*args,**kwargs):
        student = User.objects.get(pk=pk)
        orders = LessonOrder.objects.filter(order__user=student)
        serializer = LessonOrderSerializer(orders,many=True)
        return Response(serializer.data)

class LessonOrdersTeacherHistoricView(generics.ListAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = LessonOrderSerializer
    queryset = LessonOrder.objects.all()

    def get(self,request,pk,*args,**kwargs):
        teacher = Teacher.objects.get(pk=pk)
        orders = LessonOrder.objects.filter(teacher=teacher)
        serializer = LessonOrderSerializer(orders,many=True)
        return Response(serializer.data)
    

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
    serializer_class = BookOrderSerializer
    queryset = BookOrder.objects.all()

    def delete(self,request,pk):
        lesson_order = get_object_or_404(LessonOrder,pk=pk)
        order = lesson_order.order
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookOrderView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = BookOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return BookOrder.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class BookOrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = BookOrderSerializer
    queryset = BookOrder.objects.all()

    def delete(self,request,pk):
        book_order = get_object_or_404(BookOrder,pk=pk)
        order = book_order.order
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    #? Specific pagination
    pagination_class = CustomPagination
    
class DocumentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    #? Specific pagination
    pagination_class = CustomPagination

class DocumentCreateView(generics.CreateAPIView):
    permission_classes = [IsTeacher]
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(uploader=user)

    def perform_create(self,serializer):
        serializer.save()
        return Response(self.request.data,status=status.HTTP_201_CREATED)

class DocumentRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

class LibrairyView(generics.ListAPIView):
    permission_classes = [IsCurrentUserOrAdmin]
    serializer_class = DocumentSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        user = User.objects.get(pk=pk)
        return Document.objects.filter(uploader=user)

class FormationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FormationSerializer

    queryset = Formation.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FormationSerializer(queryset, many=True)
        return Response(serializer.data)

