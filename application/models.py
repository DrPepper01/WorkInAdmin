from django.db import models
# from django.db.models import ForeignKey, ManyToManyField


class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name} | {self.date_of_birth}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='bookies')

    def __str__(self):
        return f'{self.title} | {self.info} | {self.price}'

    class Meta:
        ordering = ('title', )


class Janre(models.Model):
    name = models.CharField(max_length=20)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    age = models.IntegerField()
    courses = models.ManyToManyField('Courses')
    student_average_grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} | {self.surname} | {self.student_average_grade}'


class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    # students = models.ManyToManyField('Students', on_delete=models.CASCADE, null=True, blank=True)
    date_of_start = models.DateField()
    date_of_the_end = models.DateField()

    def __str__(self):
        return f'{self.title} | {self.date_of_start} | {self.date_of_the_end}'




