from rest_framework import mixins, viewsets, permissions
from rest_framework.exceptions import ValidationError

from event.models.participant import Participant
from event.serializers.participant import ParticipantSerializer


class ParticipantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        user = self.request.user
        event = self.kwargs['event']
        if Participant.objects.filter(user=user, event_id=event).exists():
            raise ValidationError("Już jesteś zapisany na to wydarzenie.")
        serializer.save(user=user, event_id=event)
