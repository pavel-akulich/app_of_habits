from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar', 'telegram_id',)
