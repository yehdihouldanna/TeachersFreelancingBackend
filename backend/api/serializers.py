# from django.contrib.auth.models import User
from rest_framework import serializers
from backend.models import Document, Order, LessonOrder, BookOrder , Book, School, Formation
from user_app.models import User, Student, Teacher 
from backend.models_basic import SUBJECTS,Subject
from backend.utils.utils import *
from user_app.api.serializers import StudentSerializer, UserSerializer
from django.core.files.base import ContentFile, File
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

    def create(self,validated_data):
        # username = self.initial_data["uploader"]
        user =  self.context['request'].user
        if self.initial_data['file']:
            extension = self.initial_data['file'].name.split(".")[-1]
            name=self.validated_data["title"]+'by'+user.username+"."+extension
            file = File(self.initial_data['file'], name=name)
        else :
            file= None
        try:
            validated_data.pop("file")
        except :
            pass
        document= Document.objects.create(uploader=user,file=file,**validated_data)
        document.save()
        return document

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

class BookOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = BookOrder
        fields = '__all__'
    
    def create(self,validated_data):
        order_data = validated_data.pop("order")
        username = self.initial_data['order']["username"]
        user = User.objects.get(username=username)
        order= Order.objects.create(user=user,**order_data)
        order.save()

        book_order = BookOrder.objects.create(order=order,**validated_data)

        return book_order


class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = '__all__'

class FormationSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = Formation
        fields = '__all__'
