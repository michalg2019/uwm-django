from rest_framework import serializers

from event.models.participant import Participant
from user.serializers.user import ShortUserSerializer


class ParticipantSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Participant
        fields = '__all__'
        read_only_fields = ['joined_at', 'event']