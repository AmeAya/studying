from rest_framework.serializers import ModelSerializer

from .models import *


class StudentTypeSerializer(ModelSerializer):
    class Meta:
        model = StudentType
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        representation['type'] = StudentTypeSerializer(instance=instance.type, many=False).data
        representation['subjects'] = SubjectSerializer(instance=instance.subjects.all(), many=True).data
        return representation


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        representation['student'] = StudentSerializer(instance=instance.student, many=False).data
        representation['subject'] = SubjectSerializer(instance=instance.subject, many=False).data
        representation['date'] = instance.date.strftime("%d.%m.%Y  %H:%M")
        return representation


class PackSerializer(ModelSerializer):
    class Meta:
        model = Pack
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        representation['student'] = StudentSerializer(instance=instance.student, many=False).data
        representation['pack'] = PackSerializer(instance=instance.pack, many=False).data
        representation['date'] = instance.date.strftime("%d.%m.%Y  %H:%M")
        return representation


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
