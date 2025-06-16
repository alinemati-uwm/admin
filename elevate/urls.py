
from django.contrib import admin
from django.urls import path , include

from django.conf.static import static
from django.conf import settings


urlpatterns = [
    
    path("admin/", admin.site.urls),

#    path('captcha/', include('captcha.urls')),
] + 
