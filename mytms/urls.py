"""
URL configuration for mytms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from apps.tms.urls import router as tms_router
from apps.tms.urls import urlpatterns as tms_urlpatterns
from django.contrib import admin
from django.urls import path

from mytms.settings import ADMIN_URL

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
]


from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from mytms.swagger_schema_generator import SwaggerSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="My TMS",
        default_version="v1",
        description="My TMS",
        contact=openapi.Contact(email="seunfunmi.adegoke@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=SwaggerSchemaGenerator,
)


urlpatterns = [path("admin/", admin.site.urls), path("tms/", include(tms_router.urls))]


if settings.DEBUG is True:
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path("debug", include("debug_toolbar.urls")),
    ]


urlpatterns.extend(tms_urlpatterns)
admin.site.site_header = "My TMS"
