from django.test import TestCase

from bureau.models import Topic


# Create your tests here.
class ModelCreateTestCase(TestCase):
    def test_create_topic(self):
        topic = Topic.objects.create(name="hello")
        self.assertEqual(topic.name, "hello")
