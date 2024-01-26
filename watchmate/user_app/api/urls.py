from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_app.api.views import registration_view, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='registration'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
