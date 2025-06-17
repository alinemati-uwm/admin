
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse

from django.conf.urls.static import static  

from django.conf import settings
from education.admin import education_site

urlpatterns = [
    path("admin/", admin.site.urls),
   # path("", lambda request: HttpResponse("✅ Welcome to the homepage!")),
    path("education-admin/", education_site.urls),  # Custom admin for education app
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
