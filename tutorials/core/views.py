from typing import Coroutine
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
import pandas as pds
from core import models
from core.permissions import IsOwner
from core.serializers import (
    CourseListSeralizer,
    SectionListSeralizer,
    LectureListSeralizer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import CourseList, SectionList, LectureList


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


class FileView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    # Code for creation
    def post(self, request, format=None):
        file = request.FILES['file'].read()
        xls = pds.ExcelFile(file)
        # print(xls.sheet_names)
        for sheet_name in xls.sheet_names:
            print('sheets: ', sheet_name)
            df = xls.parse(sheet_name)
            rows, cols = df.shape
            for row in range(0, rows):
                row_data = df.loc[row].to_dict()
                if 'Course' in sheet_name:
                    b = CourseList.objects.create(title=row_data['title'], user=self.request.user)
                    b.save()
                elif 'Section' in sheet_name:
                    course_obj = CourseList.objects.get(title=row_data['course'])
                    # print(course_obj.id)
                    # print(course_obj, dir(course_obj))
                    b = SectionList.objects.create(title=row_data['title'], course=course_obj, user=self.request.user)
                    b.save()
                elif 'Lectures' in sheet_name:
                    section_obj = SectionList.objects.get(title=row_data['section'])
                    b = LectureList.objects.create(title=row_data['title'], section=section_obj, user=self.request.user)
                    b.save()

        return Response ({            
            "message":"All Excel data posted Successfully.",
            "status" : True,
        })
