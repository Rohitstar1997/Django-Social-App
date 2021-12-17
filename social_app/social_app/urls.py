"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core import views


schema_view = get_schema_view(
    openapi.Info(
        title="Social Auth",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include(('core.urls', 'core'),
                                 namespace="social_auth")),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    # path("login/", views.login, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('social-auth/', include('social_django.urls', namespace="social")),
    # # path("home/", views.home, name="home"),
]

# from dj_rest_auth.registration.views import (
#     SocialAccountListView, SocialAccountDisconnectView
# )

# urlpatterns += [
#     path(
#         'api/v1/socialaccounts/',
#         SocialAccountListView.as_view(),
#         name='social_account_list'
#     ),
#     path(
#         'api/v1/socialaccounts/<int:pk>/disconnect/',
#         SocialAccountDisconnectView.as_view(),
#         name='social_account_disconnect'
#     )
# ]