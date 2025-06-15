from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, permissions, filters

from event.models import Pogoda
from event.serializers.event import EventSerializer


class EventViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Pogoda.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['start_date', 'location']
    search_fields = ['name', 'description']
    ordering_fields = ['start_date', 'name']

    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)