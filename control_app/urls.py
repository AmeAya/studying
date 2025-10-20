from django.urls import path

from .views import *

urlpatterns = [
    path('student_type', StudentTypeApiView.as_view()),
    path('student', StudentApiView.as_view()),
    path('lesson', LessonApiView.as_view()),
    path('pack', PackApiView.as_view()),
    path('payment', PaymentApiView.as_view()),
    path('subject', SubjectApiView.as_view()),
]
