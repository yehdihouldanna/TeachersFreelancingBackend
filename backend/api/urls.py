from django.urls import path, include
from backend.api.views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # path('login/',obtain_auth_token,name="login"),
    path('lesson_order/',LessonOrderView.as_view(),name="lesson_order"),
    path('modify_lesson_order/<int:pk>/',LessonOrderRUDView.as_view(),name="modify_lesson_order"),
    path('book_order/',BookOrderView.as_view(),name="book_order"),
    path('modify_book_order/<int:pk>/',BookOrderRUDView.as_view(),name="modify_book_order"),
    path('formation_list/',FormationListView.as_view(),name="formation_list"),
    path('list_books/',BookListView.as_view(),name="list_books"),
    path('list_documents/',DocumentListView.as_view(),name="list_documents"),
    path('document_create/',DocumentCreateView.as_view(),name="document_create"),
    path('document_details/<int:pk>/',DocumentRUDView.as_view(),name="document_details"),
    path('librairy/<int:pk>',LibrairyView.as_view(),name="librairy"),
    path('teacher_historic/<int:pk>/',LessonOrdersTeacherHistoricView.as_view(),name="teacher_historic"),
    path('student_historic_lesson/<int:pk>/',LessonOrdersStudentHistoricView.as_view(),name="student_historic_lesson"),
    path('student_historic_book/<int:pk>/',BookOrdersStudentHistoricView.as_view(),name="student_historic_book"),
    path('teacher/<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    # path('lesson_order_review/<int:pk>/',ReviewDetail.as_view(),name="review-detail"),
    path('teacher_review/<int:pk>/',ReviewDetail.as_view(),name="review-detail"),
]


if settings.DEBUG:
    urlpatterns += [
        path('document_files/', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
    # urlpatterns += [
    #     path(r'^media/(?P<path>.*)$', serve, {
    #         'document_root': settings.MEDIA_ROOT,
    #     }),
    #     path(r'^static/(?P<path>.*)$', serve, {
    #         'document_root': settings.STATIC_ROOT,
    #     }),
    # ]