from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# Create your models here.
class CourseList(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    ## auto_now_add 1st time create set to current value
    created_on = models.DateTimeField(auto_now_add=True)
    ## auto_now update time update set to current value
    updated_on = models.DateTimeField(auto_now=True)
    ## adding login security, which user is adding 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SectionList(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(CourseList, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ## adding login security, which user is adding 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LectureList(models.Model):
    title = models.CharField(max_length=100)
    section = models.ForeignKey(SectionList, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ## adding login security, which user is adding 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
