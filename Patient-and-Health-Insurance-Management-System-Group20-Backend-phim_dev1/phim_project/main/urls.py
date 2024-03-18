from django.urls import path, include
from main.views import health_check


urlpatterns = [
    path('',health_check, name='health_check'),
    path('auth/', include('authentication.urls')),
]