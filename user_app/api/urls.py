from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import log_out_view, registration_view,login_view,register_teacher_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView , TokenVerifyView


# TODO revert from jwt to the classical django token auth.
urlpatterns = [
    # path('login/',obtain_auth_token,name="login"),
    path('login/',login_view,name="login"),
    path('register/',registration_view,name='register'),
    path('logout/',log_out_view, name='logout'),
    path('register_teacher/',register_teacher_view,name='regisster_teacher'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]