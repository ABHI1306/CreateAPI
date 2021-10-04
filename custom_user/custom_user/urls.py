from django.contrib import admin
from django.urls import path

admin.site.site_header = "Login with Email or Mobile"

urlpatterns = [
    path('admin/', admin.site.urls),
]
