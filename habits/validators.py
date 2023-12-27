from rest_framework import serializers


def validator_exclude_award_and_related_habit(value):
    """
    Validate that selecting both a related habit and specifying an award is not allowed.

    Args:
        value (dict): Dictionary containing data to be validated.

    Raises:
        serializers.ValidationError: Raised if both a related habit and an award are selected simultaneously.
    """

    award = value.get('award')
    related_habit = value.get('related_habit')

    if award and related_habit:
        raise serializers.ValidationError(
            'Simultaneous selection of a related habit and indication of a reward is prohibited')


def validator_time_to_complete(value):
    """
    Validator for the time it takes to complete a habit.

    Args:
        value (int): Time in seconds.

    Raises:
        serializers.ValidationError: Raised if the time to complete is greater than the maximum allowed time.
    """

    max_time = 120
    if value > max_time:
        raise serializers.ValidationError(f'The execution time should be no more than {max_time} seconds')


def validator_related_habit(value):
    """
    Validator to ensure that only pleasant habits can be related.

    Args:
        value (Habit): Instance of the related habit.

    Raises:
        serializers.ValidationError: Raised if the related habit does not have the attribute 'is_pleasant' set to True.
    """

    if not value.is_pleasant:
        raise serializers.ValidationError('A related habit should have the hallmark of a pleasant habit')


def validator_not_award_or_related_habit(value):
    """
    Validator to ensure that pleasant habits cannot have an award or related habit.

    Args:
        value (dict): Dictionary containing data to be validated.

    Raises:
        serializers.ValidationError: Raised if a pleasant habit has an award or a related habit specified.
    """

    is_pleasant = value.get('is_pleasant')
    award = value.get('award')
    related_habit = value.get('related_habit')

    if is_pleasant and (award or related_habit is not None):
        raise serializers.ValidationError('A pleasant habit cannot have a reward or a related habit.')


def validator_frequency(value):
    """
    Validator for the frequency of habit execution.

    Args:
        value (int): Frequency value.

    Raises:
        serializers.ValidationError: Raised if the frequency is greater than the maximum allowed frequency.
    """

    max_frequency = 7
    if value > max_frequency:
        raise serializers.ValidationError(f'You should not perform the habit less than once every {max_frequency} days')
