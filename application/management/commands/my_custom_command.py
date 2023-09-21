from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from application.models import Students, Courses


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Получаем список всех курсов
        courses = Courses.objects.all()

        # Выводим список студентов для каждого курса
        for course in courses:
            students = course.stud.all()
            self.stdout.write(f"Студенты для курса '{course.title}':")
            for student in students:
                self.stdout.write(f"- {student.name}")

        # Получаем список всех студентов
        students = Students.objects.all()

        # Выводим список курсов для каждого студента
        for student in students:
            courses = student.courses.all()
            self.stdout.write(f"Курсы для студента '{student.name}':")
            for course in courses:
                self.stdout.write(f"- {course.title}")


class NewCommand(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых Студентов и курсов')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            Students.objects.create(name=get_random_string(length=7), surname='',
                                    age='20')
            Courses.objects.create(title=get_random_string(length=5))
