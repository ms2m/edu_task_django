from rest_framework import serializers
from core.models import CourseList, SectionList, LectureList


class LectureListSeralizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = LectureList
        fields = '__all__'


class SectionListSeralizer(serializers.ModelSerializer):
    items = LectureListSeralizer(source='lecturelist_set', many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SectionList
        fields = '__all__'


class CourseListSeralizer(serializers.ModelSerializer):
    ## user value will be saved the current users who is logged in.
    items = SectionListSeralizer(source='sectionlist_set', many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CourseList
        fields = '__all__'
