from graphene_django.views import GraphQLView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class AuthenticatedGraphQLView(GraphQLView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        user_auth = JWTAuthentication()
        try:
            user, token = user_auth.authenticate(request)
            if user:
                request.user = user
        except Exception:
            pass

        return super().dispatch(request, *args, **kwargs)