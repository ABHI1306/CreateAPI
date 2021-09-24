from django.contrib import admin
from django.urls import path, include
from updates.views import json_example_view, JsonCBV, JsonCBV2, SerializedDetailView, SerializedListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.api.urls')),
    path('api/status/', include('status.api.urls')),
    path('api/updates/', include('updates.api.urls')),
]
