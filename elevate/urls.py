
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from education.admin import education_site

urlpatterns = [
    path("admin/", admin.site.urls),
   # path("", lambda request: HttpResponse("✅ Welcome to the homepage!")),
    path("education-admin/", education_site.urls),  # Custom admin for education app
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
