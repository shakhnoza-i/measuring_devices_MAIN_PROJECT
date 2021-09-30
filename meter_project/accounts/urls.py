from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from accounts.views import LogoutView, RegistrationView, SearchUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #path('login/', obtain_auth_token, name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search_user/', SearchUserView.as_view(), name='search_user'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]