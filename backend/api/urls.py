from django.urls import path, include
from backend.api.views import LessonOrderView,DocumentOrderView,DocumentView


urlpatterns = [
    # path('login/',obtain_auth_token,name="login"),
    path('lesson_order/',LessonOrderView.as_view(),name="lesson_order"),
    path('document_order/',DocumentOrderView.as_view(),name="document_order"),
    path('document/',DocumentView.as_view(),name="document")
]