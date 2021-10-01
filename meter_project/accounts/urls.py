from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from accounts.views import logout_view, registration_view, SearchUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('search_user/', SearchUserView.as_view(), name='search_user'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]