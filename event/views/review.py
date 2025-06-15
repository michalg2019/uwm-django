from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from event.models import Pogoda
from event.models.review import Review
from event.serializers.review import ReviewSerializer


class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        event = get_object_or_404(Pogoda, pk=self.kwargs['event'])
        if Review.objects.filter(user=self.request.user, event=event).exists():
            raise serializers.ValidationError({
                "detail": "Już dodałeś recenzję do tego wydarzenia."
            })

        serializer.save(user=self.request.user, event=event)

    @action(detail=False, methods=['get'], url_path='avg-rating', url_name='avg-rating')
    def avgrating(self, request, *args, **kwargs):
        event = get_object_or_404(Pogoda, pk=self.kwargs['event'])

        rating = Review.objects.filter(event=event).aggregate(avg=Avg('rating'))
        return Response(rating)