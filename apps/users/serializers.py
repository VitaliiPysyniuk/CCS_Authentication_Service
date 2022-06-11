from rest_framework.serializers import ModelSerializer

from .models import CustomAuthUserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomAuthUserModel
        fields = '__all__'

    def create(self, validated_data):
        return CustomAuthUserModel.objects.create_user(**validated_data)


class ShortUserSerializer(ModelSerializer):
    class Meta:
        model = CustomAuthUserModel
        fields = ['id', 'first_last_name', 'phone_number']
