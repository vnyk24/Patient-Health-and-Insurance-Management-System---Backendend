from django.contrib import admin
from django.urls import path
from auth_app.views import signIn,postSign

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signIn, name='signin'),  
    path('postSign/', postSign, name='postsign'),  
]
