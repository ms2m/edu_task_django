from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from core import models
from core.permissions import IsOwner
from core.serializers import (
    CourseListSeralizer,
    SectionListSeralizer,
    LectureListSeralizer
)


class CourseListsAPIView(ListCreateAPIView):
    """
    Listing, Creation
    """
    ## converting into genric view.
    serializer_class = CourseListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = models.CourseList.objects.filter(user=self.request.user)
        return queryset


class SectionListsAPIView(ListCreateAPIView):
    """
    Listing, Creation
    """
    ## converting into genric view.
    serializer_class = SectionListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = models.SectionList.objects.filter(user=self.request.user)
        return queryset


class LectureListsAPIView(ListCreateAPIView):
    """
    Listing, Creation
    """
    serializer_class = LectureListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        queryset = models.LectureList.objects.filter(user=self.request.user)
        return queryset


class LectureListAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrivel, Update, Destroy
    """
    serializer_class = LectureListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = models.LectureList.objects.filter(user=self.request.user)
        return queryset
