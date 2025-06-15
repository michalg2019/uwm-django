from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from user.views.admin import UserManageViewSet
from user.views.user import UserViewSet

drf_router = routers.DefaultRouter()
drf_router.register('user', UserViewSet, basename='user')
drf_router.register('manage/user', UserManageViewSet, basename='manage-user')

urlpatterns = drf_router.urls + [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]