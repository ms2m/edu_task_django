from django.contrib import admin
from core.models import CourseList, SectionList, LectureList


# Register your models here.
admin.site.register(CourseList)
admin.site.register(SectionList)
admin.site.register(LectureList)

