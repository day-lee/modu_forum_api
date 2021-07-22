from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('modu_forum_api.urls', namespace='modu_forum_api')),
]
