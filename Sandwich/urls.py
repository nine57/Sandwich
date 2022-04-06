from django.urls import include, path, re_path
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Making Sandwich",
        default_version='v1',
        description="Making Sandwich API",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # django apps
    path('sandwiches', include('sandwiches.urls')),
    path('ingredients', include('ingredients.urls')),

    # swagger setting
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
