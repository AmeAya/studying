from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .functions import check_fields
from .serializers import *


class GenericApiView(APIView):
    permission_classes = (AllowAny,)
    model = None
    serializer_class = None

    def get(self, request):
        if 'id' in request.GET:
            try:
                obj = self.model.objects.get(id=request.GET['id'])
                data = self.serializer_class(instance=obj, many=False).data
                return Response(data=data, status=status.HTTP_200_OK)
            except self.model.DoesNotExist:
                return Response(
                    {'message': f"Object with id {request.GET['id']} not exist!"},
                    status=status.HTTP_404_NOT_FOUND
                )

        objects = self.model.objects.all()
        data = self.serializer_class(objects, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_fields(['id'])
    def patch(self, request):
        try:
            obj = self.model.objects.get(id=request.GET['id'])
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except self.model.DoesNotExist:
            return Response(
                {'message': f"Object with id {request.GET['id']} not exist!"},
                status=status.HTTP_404_NOT_FOUND
            )

    @check_fields(['id'])
    def delete(self, request):
        try:
            obj = self.model.objects.get(id=request.GET['id'])
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response(
                {'message': f"Object with id {request.GET['id']} not exist!"},
                status=status.HTTP_404_NOT_FOUND
            )


class StudentTypeApiView(GenericApiView):
    model = StudentType
    serializer_class = StudentTypeSerializer


class StudentApiView(GenericApiView):
    model = Student
    serializer_class = StudentSerializer


class LessonApiView(GenericApiView):
    model = Lesson
    serializer_class = LessonSerializer


class PackApiView(GenericApiView):
    model = Pack
    serializer_class = PackSerializer


class PaymentApiView(GenericApiView):
    model = Payment
    serializer_class = PaymentSerializer


class SubjectApiView(GenericApiView):
    model = Subject
    serializer_class = SubjectSerializer
