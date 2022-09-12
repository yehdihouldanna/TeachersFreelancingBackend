from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import AccountRechargeView, TeacherListView, log_out_view, registration_view,login_view,register_teacher_view,register_student_view
from user_app.api.views import TeacherDetailView , StudentDetailView,AccountDetailView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView , TokenVerifyView



urlpatterns = [
    # path('login/',obtain_auth_token,name="login"),
    path('login/',login_view,name="login"),
    path('register/',registration_view,name='register'),
    path('logout/',log_out_view, name='logout'),
    path('register_teacher/',register_teacher_view,name='register_teacher'),
    path('register_student/',register_student_view,name='register_student'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('teacher/<int:pk>',TeacherDetailView.as_view(),name='teacher_details'),
    path('student/<int:pk>',StudentDetailView.as_view(),name='student_details'),
    path('teachers_list/',TeacherListView.as_view(),name="teachers_list"),

    path('account_details/<user__username>',AccountDetailView.as_view(),name="account_details"),
    path('account_recharge/<user__username>',AccountRechargeView.as_view(),name="account_details"),
    
]