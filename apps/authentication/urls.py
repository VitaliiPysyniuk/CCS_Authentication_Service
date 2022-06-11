from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='authenticate_user'),
    path('/refresh', TokenRefreshView.as_view(), name='refresh_tokens_pair'),
    path('/verify', TokenVerifyView.as_view(), name='verify')
]
