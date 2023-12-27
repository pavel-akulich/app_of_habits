from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Award(models.Model):
    """
    Model for representing awards.

    Attributes:
        user (ForeignKey): The user associated with the award.
        reward (TextField): The reward for completing a habit.

    Methods:
        __str__: Returns a string representation of the award.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    reward = models.TextField(verbose_name='вознаграждение за выполнение')

    def __str__(self):
        return f'{self.user} - {self.reward}'

    class Meta:
        verbose_name = 'вознаграждение'
        verbose_name_plural = 'вознаграждения'


class Habit(models.Model):
    """
    Model for representing habits.

    Attributes:
        user (ForeignKey): The user associated with the habit.
        award (ForeignKey): The award associated with the habit.
        place (CharField): The place where the habit is performed.
        execution_time (TimeField): The time when the habit is performed.
        action (TextField): The action associated with the habit.
        is_pleasant (BooleanField): A flag indicating whether the habit is pleasant.
        related_habit (ForeignKey): A related habit associated with the habit.
        frequency (PositiveIntegerField): The frequency of the habit in days.
        time_to_complete (PositiveIntegerField): The time required to complete the habit.
        is_published (BooleanField): A flag indicating whether the habit is published.

    Methods:
        __str__: Returns a string representation of the habit.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    award = models.ForeignKey(Award, on_delete=models.SET_NULL, verbose_name='вознаграждение', **NULLABLE)

    place = models.CharField(max_length=200, verbose_name='место выполнения привычки')
    execution_time = models.TimeField(verbose_name='время выполнения привычки')
    action = models.TextField(verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL, verbose_name='связанная привычка',
                                      related_name='related_habits')

    frequency = models.PositiveIntegerField(default=1, verbose_name='периодичность в днях')
    time_to_complete = models.PositiveIntegerField(verbose_name='время на выполнение')
    is_published = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.execution_time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
