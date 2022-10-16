from rest_framework import serializers
from backend.models_basic import SUBJECTS,Subject,Classe,Specialty ,Disponibility

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'
class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
class DisponibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibility
        fields = '__all__'