from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from backend import settings

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields  = ['id',"username", "email", 'first_name', "last_name", "password"]