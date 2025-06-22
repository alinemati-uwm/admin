
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse

from django.conf.urls.static import static  

from django.conf import settings
from education.admin import education_site


from django.contrib.auth.models import User

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin



class OTPAdmin(OTPAdminSite):
   pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)


urlpatterns = [
    path("admin/", admin_site.urls),
    # path("admin/", admin.site.urls),
   # path("", lambda request: HttpResponse("✅ Welcome to the homepage!")),
    path("education-admin/", education_site.urls),  # Custom admin for education app
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
