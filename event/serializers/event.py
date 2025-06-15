from rest_framework import serializers

from event.models.pogoda import Pogoda
from event.models.participant import Participant
from event.serializers.participant import ParticipantSerializer
from event.serializers.review import ReviewSerializer
from user.serializers.user import ShortUserSerializer


class EventSerializer(serializers.ModelSerializer):
    organizer = ShortUserSerializer(read_only=True)
    participants = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Pogoda
        fields = '__all__'

    def get_participants(self, obj):
        participants = Participant.objects.filter(pogoda=obj)
        return ParticipantSerializer(participants, many=True).data

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        return super().create(validated_data)

    class PogodaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pogoda
            fields = ['id', 'name', 'description', 'start_date', 'end_date', 'location', 'type', 'organizer']

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            # Make the response more readable
            representation['type_display'] = instance.get_type_display()
            return representation