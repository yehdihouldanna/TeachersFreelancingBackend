
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [

    #? SWAGGER urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('admin/', admin.site.urls),
    path('account/',include('user_app.api.urls')),
    path('',include('backend.api.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
] + i18n_patterns(
    # ...
    path('admin/', admin.site.urls),
    # ...
 
    # If no prefix is given, use the default language
    prefix_default_language=True
)

# urlpatterns += i18n_patterns(url(r'^admin/', admin.site.urls))
