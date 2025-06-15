from rest_framework import serializers

from event.models.review import Review
from user.serializers.user import ShortUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at', 'event']