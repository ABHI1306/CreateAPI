from django.contrib import admin
from django.urls import path, include
from updates.views import json_example_view, JsonCBV, JsonCBV2, SerializedDetailView, SerializedListView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/updates/', include('updates.api.urls')),

    # path('api/updates/', include('updates.api.urls')),
    # path('json/example/',json_example_view),
    # path('json/CBV/',JsonCBV.as_view()),
    # path('json/CBV2/',JsonCBV2.as_view()),
    # path('json/detail/',SerializedDetailView.as_view()),
    # path('json/list/',SerializedListView.as_view()),
]
