from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User
from user.serializers.user import UserSerializer


class UserViewSet(GenericViewSet, mixins.RetrieveModelMixin):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	authentication_classes = (JWTAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated,
	)

	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@action(detail=False, methods=['get'], url_path='current', url_name='current_user')
	def current_user(self, request):
		return Response(
			self.get_serializer(request.user).data
		)
