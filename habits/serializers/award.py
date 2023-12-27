from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Award
from users.models import User


class AwardSerializer(serializers.ModelSerializer):
    """
    Serializer for the Award model.

    Attributes:
        user (SlugRelatedField): SlugRelatedField to represent the user by email.
    """

    user = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)

    class Meta:
        model = Award
        fields = ('pk', 'user', 'reward',)
