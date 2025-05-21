from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect



schema_view = get_schema_view(
    openapi.Info(
        title="Mintaqalar API",
        default_version='v1',
        description="Foydalanuvchilar va mintaqalar API hujjatlari",
        contact=openapi.Contact(email="admin@gmail.com")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',lambda request: redirect('/swagger/')),
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('regions.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0),name='schema-json'),
]