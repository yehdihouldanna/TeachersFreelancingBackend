# from django.contrib.auth.models import User
from django.core.files.base import File
from django.db import transaction
from rest_framework import serializers

from backend.api.serializers_basic import *
from backend.models import (Book, BookOrder, Document, Formation, LessonOrder,
                            Order, Review, School)
from backend.models_basic import  Subject
from backend.utils.utils import *
from user_app.models import User


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
           slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class LessonOrderSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    classes = ClasseSerializer(many=True,read_only=True) 
    subjects=  SubjectSerializer(many=True,read_only=True)
    class Meta:
        model = LessonOrder
        fields ='__all__'

    @transaction.atomic
    def create(self,validated_data):
        try :
            with transaction.atomic():
                order_data = validated_data.pop("order")
                username = self.initial_data['order']["username"]
                user = User.objects.get(username=username)
                order= Order.objects.create(user=user,**order_data)
                order.save()
                subjects = []
                classes = []
                if 'subjects' in self.initial_data.keys():
                    try : 
                        if 'subjects' in validated_data.keys():
                            subjects = validated_data.pop("subjects")
                        else :
                            subjects = self.initial_data['subjects']
                        assert(type(subjects)==list)
                    except :
                        raise serializers.ValidationError({"error": f" Expected 'subjects' of type 'list' but got {type(subjects)}"})
                if 'classes' in self.initial_data.keys():
                    try : 
                        if 'classes' in validated_data.keys():
                            classes = validated_data.pop("classes")
                            
                        else :
                            classes = self.initial_data['classes']
                        assert(type(classes)==list)
                    except :
                        raise serializers.ValidationError({"error": f" Expected 'subjects' of type 'list' but got {type(subjects)}"})
                lesson_order = LessonOrder.objects.create(order=order,**validated_data)

                for subject in subjects:
                    try : 
                        sujet = Subject.objects.get(name=subject)
                        lesson_order.subjects.add(sujet)
                    except : 
                        raise serializers.ValidationError({'error': f' Subject "{sujet}" does not exist'})
                for classe in classes:
                    try :
                        cla = Classe.objects.get(name=classe)
                        lesson_order.classes.add(cla)
                    except : 
                        raise serializers.ValidationError({'error': f' Classe "{classe}" does not exist'})

                return lesson_order
        except  serializers.ValidationError as error:
            raise serializers.ValidationError(error.args)

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
    books = BookSerializer(many=True,read_only=True)
    class Meta:
        model = BookOrder
        fields = '__all__'
    
    @transaction.atomic
    def create(self,validated_data):
        try :
            with transaction.atomic():
                order_data = validated_data.pop("order")
                username = self.initial_data['order']["username"]
                user = User.objects.get(username=username)
                try : 
                    suj = validated_data.pop("subject")
                    subject = Subject.objects.get(name=suj)
                except : 
                    raise serializers.ValidationError({'error': f' Subject "{suj}" does not exist'})
                try : 
                    cla = validated_data.pop("classe")
                    classe = Classe.objects.get(name=cla)
                except : 
                    raise serializers.ValidationError({'error': f' Classe "{cla}" does not exist'})
                books=[]
                
                if 'books' in self.initial_data.keys():
                    try : 
                        books = validated_data.pop("books")
                        assert type(books)==list
                    except :
                        try :
                            books = self.initial_data['books']
                            assert type(books)==list
                        except :
                            raise serializers.ValidationError({"error": f" Expected 'books' of type 'list' but got {type(books)}"})
                        
                order= Order.objects.create(user=user,**order_data)
                order.save()

                book_order = BookOrder.objects.create(order=order,**validated_data,subject=subject,classe=classe)
              
                for book in books:
                    try :
                        book = Book.objects.get(pk=book)
                        book_order.books.add(book)
                    except : 
                        raise serializers.ValidationError({'error': f' Book "{book}" does not exist'})

                return book_order
        except  serializers.ValidationError as error:
            raise serializers.ValidationError(error.args)


class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = '__all__'

class FormationSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = Formation
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta : 
        model = Review
        fields= "__all__"
        # exlude=("lesson_order")
        exlude=("teacher")
