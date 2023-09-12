from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from application.models import Students, Courses


class Command(BaseCommand):
    help = u'Создание случайных студентов'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых Студентов')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            Students.objects.create(name=get_random_string(length=7), surname='',
                                    age='20')
