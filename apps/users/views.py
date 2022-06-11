from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CustomAuthUserModel
from .serializers import UserSerializer, ShortUserSerializer
from .permissions import IsAdminUser


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomAuthUserModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomAuthUserModel.objects.all()
    permission_classes = [AllowAny]


class AuthenticatedUserRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShortUserSerializer
    queryset = CustomAuthUserModel.objects.all()

    def get_object(self):
        return self.request.user


