from django.urls import path, include
from backend.api.views import LessonOrderView,LessonOrderRUDView,DocumentOrderView,DocumentView,FormationListView,DocumentOrderRUDView


urlpatterns = [
    # path('login/',obtain_auth_token,name="login"),
    path('lesson_order/',LessonOrderView.as_view(),name="lesson_order"),
    path('modify_lesson_order/<int:pk>/',LessonOrderRUDView.as_view(),name="modify_lesson_order"),
    path('document_order/',DocumentOrderView.as_view(),name="document_order"),
    path('modify_document_order/<int:pk>/',DocumentOrderRUDView.as_view(),name="modify_document_order"),
    path('formation_list/',FormationListView.as_view(),name="formation_list"),

    path('document/',DocumentView.as_view(),name="document")
]