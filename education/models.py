from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Course(models.Model):
    Course_title = models.CharField(_("Course Title"), max_length=200)
    Course_description = models.TextField(_("Course Description"))
    Course_start_date = models.DateField(_("Course Start Date"))
    Course_end_date = models.DateField(_("Course End Date"))
    Course_instructor = models.CharField(_("Course Instructor"), max_length=100)

    slug = models.SlugField(_("Slug"), max_length=200)

    def __str__(self):
        return self.Course_title
    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ['Course_title']


class Lesson(models.Model):
    lesson_name = models.CharField(_("Lesson Name"), max_length=200)
    lesson_content = models.TextField(_("Lesson Content"))
    lesson_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name=_("Course"))
    lesson_order = models.PositiveIntegerField(_("Lesson Order"))

    slug = models.SlugField(_("Slug"), max_length=200)

    def __str__(self):
        return self.lesson_name
    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ['lesson_order']
        unique_together = ('lesson_name', 'lesson_course')
