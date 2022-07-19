from django.test import TestCase
import datetime
from django.utils import timezone
from .models import AllCources
# Create your tests here.

class AllCourcesModel(TestCase):
    def test_was_piblished(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=AllCources(startedfrom=time)
        self.assertIs(future_question.was_published(),False)

    def test_was_published_with_old_course(self):
        time=timezone.now()-datetime.timedelta(days=1,seconds=1)
        old_course=AllCources(startedfrom=time)
        self.assertIs((old_course.was_published(),False))

    def test_was_published_with_recent_course(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_course = AllCources(startedfrom=time)
        self.assertIs((recent_course.was_published(), True))
