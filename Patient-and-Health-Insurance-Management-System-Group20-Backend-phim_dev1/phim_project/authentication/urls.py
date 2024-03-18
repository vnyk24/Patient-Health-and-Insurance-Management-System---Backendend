from django.urls import path, include
from . import views

urlpatterns = [
    path('login/',views.login_func, name='login'),
    path('get_tokens/',views.get_tokens, name = 'tokens'),
    path('sign_up/', views.sign_up, name='sign_up'),
] 