from django.contrib import admin
from django.urls import path, include
from updates.views import json_example_view, JsonCBV, JsonCBV2, SerializedDetailView, SerializedListView 
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', include('status.api.urls')),
    path('api/updates/', include('updates.api.urls')),
    path('api/auth/jwt/', obtain_jwt_token),
    path('api/auth/jwt/refresh/', refresh_jwt_token),
]
