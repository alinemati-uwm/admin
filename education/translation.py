from modeltranslation.translator import register, TranslationOptions
from .models import Course, Lesson


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('Course_title', 'Course_description', 'Course_instructor')
    required_languages = ('de', 'es', 'fa', 'fr', 'it')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_name', 'lesson_content')
    required_languages = ('de', 'es', 'fa', 'fr', 'it')
