from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lorawan/', include('core.urls')),
    path('account/', include('user_app.urls')),
    #path('api-auth/', include('rest_framework.urls')),
]
