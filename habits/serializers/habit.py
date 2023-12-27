from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from habits import validators
from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Habit model.

    Attributes:
        time_to_complete (serializers.IntegerField): Integer field with validators for time_to_complete.
        frequency (serializers.IntegerField): Integer field with validators for frequency.
        related_habit (serializers.PrimaryKeyRelatedField): PrimaryKeyRelatedField for the related habit.
        user (SlugRelatedField): SlugRelatedField to represent the user by email.
        telegram_id (serializers.SerializerMethodField): Serializer method field for the telegram_id.

    Methods:
        get_telegram_id(obj): Returns the telegram_id from the related user.

    Meta:
        model (Habit): The Habit model.
        fields (tuple): The tuple of fields for serialization.
        validators (list): List of validators for the serializer.
    """

    time_to_complete = serializers.IntegerField(validators=[validators.validator_time_to_complete])

    frequency = serializers.IntegerField(validators=[validators.validator_frequency])

    related_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[validators.validator_related_habit],
        allow_null=True,
        required=False
    )

    user = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)

    telegram_id = serializers.SerializerMethodField()

    def get_telegram_id(self, obj):
        """
        Returns the telegram_id from the related user.

        Args:
            obj: The serialized object.

        Returns:
            int: The telegram_id or None.
        """

        return obj.user.telegram_id if obj.user else None

    class Meta:
        model = Habit
        fields = (
            'pk', 'user', 'award', 'place', 'execution_time', 'action', 'is_pleasant', 'related_habit', 'frequency',
            'time_to_complete', 'is_published', 'telegram_id',)

        validators = [
            UniqueTogetherValidator(
                queryset=Habit.objects.all(),
                fields=['award', 'related_habit', 'is_pleasant'],
            ),
            validators.validator_exclude_award_and_related_habit,
            validators.validator_not_award_or_related_habit
        ]
