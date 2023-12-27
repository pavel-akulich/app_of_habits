from django.urls import path

from habits.api_views.habit import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitPublicListAPIView
from habits.api_views.award import AwardListAPIView, AwardCreateAPIView, AwardUpdateAPIView, AwardDestroyAPIView
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/list/', HabitListAPIView.as_view(), name='habit-list'),
    path('habit/list/public/', HabitPublicListAPIView.as_view(), name='habit-public-list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),

    path('award/list/', AwardListAPIView.as_view(), name='award-list'),
    path('award/create/', AwardCreateAPIView.as_view(), name='award-create'),
    path('award/update/<int:pk>/', AwardUpdateAPIView.as_view(), name='award-update'),
    path('award/delete/<int:pk>/', AwardDestroyAPIView.as_view(), name='award-delete'),
]
