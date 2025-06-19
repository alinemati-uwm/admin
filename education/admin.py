from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from django.utils.text import slugify

from .models import Course, Lesson

# class AdminLoginArea(admin.AdminSite):
#     login_template = 'admin/login.html'
# admin_site = AdminLoginArea(name='admin')

class EducationAdminSite(admin.AdminSite):
    """
    Custom admin site for the education app.
    This can be used to create a separate admin area if needed.
    """
    site_header = "Education Admin"
    site_title = "Education Admin Portal"
    index_title = "Welcome to the Education Admin Portal"

education_site = EducationAdminSite(name='education_admin')




education_site.register(Course)
education_site.register(Lesson)

class LessonInline(admin.TabularInline):
    """
    Tabular inline for displaying lessons within a course.
    Shows lesson name, order, and a preview of content.
    """
    model = Lesson
    extra = 1
    max_num = 10  # Limit to 10 lessons
    fields = ('lesson_name', 'lesson_order', 'slug', 'content_preview')
    prepopulated_fields = {"slug": ("lesson_name",)}
    readonly_fields = ('content_preview',)

    def content_preview(self, obj):
        """Return a truncated preview of the lesson content"""
        if obj.lesson_content:
            return obj.lesson_content[:50] + '...' if len(obj.lesson_content) > 50 else obj.lesson_content
        return '-'
    content_preview.short_description = 'Content Preview'


class LessonAdminInline(admin.StackedInline):
    """
    Optional stacked inline (expanded view) for use instead of LessonInline.
    Provides more detailed view of lesson content.
    """
    model = Lesson
    extra = 1
    max_num = 10  # Limit to 10 lessons
    fields = ('lesson_name', 'lesson_content', 'lesson_order', 'slug')
    prepopulated_fields = {"slug": ("lesson_name",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin configuration for Course model.
    Provides comprehensive management interface for courses with filtering,
    searching, and inline lesson management.
    """
    list_display = ('id', 'Course_title', 'Course_instructor',
                    'date_range', 'lesson_count')
    list_filter = ('Course_start_date', 'Course_end_date', 'Course_instructor')
    search_fields = ('Course_title', 'Course_description', 'Course_instructor')
    ordering = ('Course_start_date',)
    prepopulated_fields = {"slug": ("Course_title",)}
    # You can switch to [LessonAdminInline] if preferred
    inlines = [LessonInline]
    date_hierarchy = 'Course_start_date'  # Adds date navigation
    actions = ['duplicate_courses']
    fieldsets = (
        (None, {
            'fields': ('Course_title', 'slug', 'Course_description')
        }),
        ('Schedule', {
            'fields': ('Course_start_date', 'Course_end_date'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
        ('Instructor', {
            'fields': ('Course_instructor',)
        }),
    )
    list_display_links = ('id', 'Course_title')

    def date_range(self, obj):
        """Display the date range in a formatted way"""
        return format_html(
            '<span style="color: #447e9b;">{}</span> to <span style="color: #447e9b;">{}</span>',
            obj.Course_start_date.strftime('%b %d, %Y'),
            obj.Course_end_date.strftime('%b %d, %Y')
        )
    date_range.short_description = 'Course Duration'

    def lesson_count(self, obj):
        """Display the number of lessons in the course"""
        count = obj.lessons.count()
        return format_html(
            '<span style="color: {};">{} lesson{}</span>',
            '#417690' if count > 0 else '#ba2121',
            count,
            's' if count != 1 else ''
        )
    lesson_count.short_description = 'Lessons'

    def get_queryset(self, request):
        """Optimize query by annotating with lesson count"""
        queryset = super().get_queryset(request)
        return queryset.annotate(lesson_count_value=Count('lessons'))

    def duplicate_courses(self, request, queryset):
        """Action to duplicate selected courses"""
        for course in queryset:
            # Create a new course with the same details
            new_course = Course.objects.create(
                Course_title=f"Copy of {course.Course_title}",
                Course_description=course.Course_description,
                Course_start_date=course.Course_start_date,
                Course_end_date=course.Course_end_date,
                Course_instructor=course.Course_instructor,
                slug=slugify(f"Copy of {course.Course_title}")
            )

            # Duplicate all lessons
            for lesson in course.lessons.all():
                Lesson.objects.create(
                    lesson_name=lesson.lesson_name,
                    lesson_content=lesson.lesson_content,
                    lesson_course=new_course,
                    lesson_order=lesson.lesson_order,
                    slug=lesson.slug
                )

        self.message_user(
            request, f"{queryset.count()} course(s) duplicated successfully.")
    duplicate_courses.short_description = "Duplicate selected courses"

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.Course_title)
        super().save_model(request, obj, form, change)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Admin configuration for Lesson model.
    Provides detailed management interface for individual lessons.
    """
    list_display = ('id', 'lesson_name', 'course_link',
                    'lesson_order', 'content_length')
    list_filter = ('lesson_course', 'lesson_order')
    search_fields = ('lesson_name', 'lesson_content',
                    'lesson_course__Course_title')
    ordering = ('lesson_course', 'lesson_order')
    prepopulated_fields = {"slug": ("lesson_name",)}
    list_display_links = ('id', 'lesson_name')
    autocomplete_fields = ['lesson_course']
    list_select_related = ('lesson_course',)
    readonly_fields = ('content_length',)
    actions = ['reorder_lessons']

    fieldsets = (
        (None, {
            'fields': ('lesson_name', 'slug', 'lesson_course', 'lesson_order')
        }),
        ('Content', {
            'fields': ('lesson_content', 'content_length'),
            'classes': ('wide',)
        }),
    )

    def course_link(self, obj):
        """Display a clickable link to the course"""
        if obj.lesson_course:
            return format_html(
                '<a href="{}">{}</a>',
                f"/admin/education/course/{obj.lesson_course.id}/change/",
                obj.lesson_course.Course_title
            )
        return '-'
    course_link.short_description = 'Course'
    course_link.admin_order_field = 'lesson_course__Course_title'

    def content_length(self, obj):
        """Display the length of the content"""
        length = len(obj.lesson_content)
        color = '#417690' if length > 200 else (
            '#f9a825' if length > 50 else '#ba2121')
        return format_html(
            '<span style="color: {};">{} characters</span>',
            color,
            length
        )
    content_length.short_description = 'Content Length'

    def reorder_lessons(self, request, queryset):
        """Action to sequentially reorder lessons in a course"""
        # Group lessons by course
        lessons_by_course = {}
        for lesson in queryset:
            if lesson.lesson_course not in lessons_by_course:
                lessons_by_course[lesson.lesson_course] = []
            lessons_by_course[lesson.lesson_course].append(lesson)

        # Reorder lessons within each course
        for course, lessons in lessons_by_course.items():
            # Sort by current order
            lessons.sort(key=lambda x: x.lesson_order)
            # Reassign order starting from 1
            for i, lesson in enumerate(lessons, 1):
                lesson.lesson_order = i
                lesson.save()

        self.message_user(request, "Selected lessons have been reordered.")
    reorder_lessons.short_description = "Reorder selected lessons sequentially"

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.lesson_name)
        super().save_model(request, obj, form, change)
