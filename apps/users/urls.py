from django.urls import path

from .views import UserCreateView, UserListView, AuthenticatedUserRetrieveView

urlpatterns = [
    path('', UserListView.as_view()),
    path('/register', UserCreateView.as_view()),
    path('/info', AuthenticatedUserRetrieveView.as_view(), name='get_data_of_authenticated_user')
]
