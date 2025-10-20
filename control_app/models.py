from django.db import models


class StudentType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True, blank=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    lessons_left = models.PositiveSmallIntegerField(default=0)

    type = models.ForeignKey(StudentType, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('Subject', blank=True)

    def __str__(self):
        return f"{self.name} - {self.type.name} {self.grade}"


class Lesson(models.Model):
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.date.strftime("%d.%m.%Y %H:%M")})"


class Pack(models.Model):
    hours = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=5000)

    def __str__(self):
        return f"{self.hours} Hours - {self.price} KZT."


class Payment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    pack = models.ForeignKey('Pack', on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.amount} KZT. ({self.date.strftime("%d.%m.%Y")})"


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
