from django.urls import path
from core.views import (
    CourseListsAPIView,
    SectionListsAPIView,
    LectureListsAPIView,
    LectureListAPIView,
    FileView,
)


urlpatterns = [
    path('api/courselists/', CourseListsAPIView.as_view()),
    path('api/sectionlists/', SectionListsAPIView.as_view()),
    path('api/lecturelists/', LectureListsAPIView.as_view()),
    path('api/lecturelist/<int:pk>/', LectureListAPIView.as_view()),
    path('file/upload/', FileView.as_view(), name='file-upload'),

]

