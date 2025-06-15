from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from event.views import EventViewSet, ParticipantViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'event', EventViewSet, basename='event')

router2 = DefaultRouter()
router2.register(r'participant', ParticipantViewSet, basename='participant')
router2.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    re_path(r'^event/(?P<event>\w+)/', include(router2.urls)),

] + router.urls
