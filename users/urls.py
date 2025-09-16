from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyApiView,
                         UserListApiView, UserRetrieveApiView,
                         UserUdateApiView)

app_name = UsersConfig.name

urlpatterns = [
              path('register/', UserCreateAPIView.as_view(), name='register'),
              path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
              path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
              path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
              path("user/", UserListApiView.as_view(), name="user_list"),
              path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrive"),
              path("user/<int:pk>/delete/", UserDestroyApiView.as_view(), name="user_delete"),
              path("user/<int:pk>/update/", UserUdateApiView.as_view(), name="user_update"),
              ]
