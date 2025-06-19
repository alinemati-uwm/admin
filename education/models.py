from django.db import models

# Create your models here.

class Course(models.Model):
    Course_title = models.CharField(max_length=200)
    Course_description = models.TextField()
    Course_start_date = models.DateField()
    Course_end_date = models.DateField()
    Course_instructor = models.CharField(max_length=100)

    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.Course_title
    class Meta:
        verbose_name_plural = "Course"
        ordering = ['Course_title']


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    lesson_content = models.TextField()
    lesson_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    lesson_order = models.PositiveIntegerField()

    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.lesson_name
    class Meta:
        verbose_name_plural = "Lesson"
        ordering = ['lesson_order']
        unique_together = ('lesson_name', 'lesson_course')
