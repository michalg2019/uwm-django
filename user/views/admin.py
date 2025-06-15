from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User
from user.serializers.user import UserSerializer


class UserManageViewSet(GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	authentication_classes = (JWTAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated,
		permissions.IsAdminUser
	)

	http_method_names = ['post', 'patch']

	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)
