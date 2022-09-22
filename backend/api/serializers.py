# from django.contrib.auth.models import User
from rest_framework import serializers
from backend.models import  Subject, Order, LessonOrder, DocumentOrder , Document, School, Formation
from user_app.models import User, Student, Teacher ,SUBJECTS
from backend.utils.utils import *
from user_app.api.serializers import StudentSerializer, UserSerializer
# Create your models here.


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
           slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class LessonOrderSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    class Meta:
        model = LessonOrder
        fields ='__all__'

    def create(self,validated_data):
        order_data = validated_data.pop("order")
        username = self.initial_data['order']["username"]
        user = User.objects.get(username=username)
        order= Order.objects.create(user=user,**order_data)
        order.save()
        subjects = validated_data.pop("subject")
        lesson_order = LessonOrder.objects.create(order=order,**validated_data)

        for subject in subjects:
            sujet = Subject.objects.get(name=subject)
            lesson_order.subject.add(sujet)

        return lesson_order

class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = '__all__'

class DocumentOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    document = DocumentSerializer()

    class Meta:
        model = DocumentOrder
        fields = '__all__'
    
    def create(self,validated_data):
        order_data = validated_data.pop("order")
        username = self.initial_data['order']["username"]
        user = User.objects.get(username=username)
        order= Order.objects.create(user=user,**order_data)
        order.save()
        document_order = DocumentOrder.objects.create(order=order,**validated_data)

        return document_order

