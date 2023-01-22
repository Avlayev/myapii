from django.urls import path
from .views import RegisterView, LoginSerializer, SetNewPasswordSerializer, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = {
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', RegisterView.as_view(), name='login'),
    path('logout/', RegisterView.as_view(), name='logout'),
    path('email-verify/', RegisterView.as_view(), name='email-verify'),
    path('token/refresh/', RegisterView.as_view(), name='token/refresh'),
    path('request-reset-eamil/', RegisterView.as_view(), name='request-reset-eamil/'),
    path('password-reset/<uidb64>/t<oken>/', RegisterView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', RegisterView.as_view(), name='password-reset-complete')

}