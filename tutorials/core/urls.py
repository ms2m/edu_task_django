from django.urls import path
from core.views import (
    CourseListsAPIView,
    SectionListsAPIView,
    LectureListsAPIView,
    LectureListAPIView,
)


urlpatterns = [
    path('api/courselists/', CourseListsAPIView.as_view()),
    path('api/sectionlists/', SectionListsAPIView.as_view()),
    path('api/lecturelists/', LectureListsAPIView.as_view()),
    path('api/lecturelist/<int:pk>/', LectureListAPIView.as_view()),
]

