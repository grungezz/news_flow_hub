from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Redactor, Topic, Newspaper
from .views import index, TopicCreateView, NewspaperListView


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("bureau:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bureau/index.html")


class TopicCreateViewTest(TestCase):
    def test_topic_create_view(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user)
        response = self.client.get(reverse("bureau:topic-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bureau/topic_form.html")


class NewspaperListViewTest(TestCase):
    def test_newspaper_list_view(self):
        response = self.client.get(reverse("bureau:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bureau/newspaper_list.html")


class RedactorDetailViewTest(TestCase):
    def test_redactor_detail_view(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user)
        redactor = Redactor.objects.create(
            username="redactor", password="redactorpassword"
        )
        response = self.client.get(
            reverse("bureau:redactor-detail", args=[redactor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bureau/redactor_detail.html")


class TopicListViewTest(TestCase):
    def test_topic_list_view(self):
        response = self.client.get(reverse("bureau:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bureau/topic_list.html")
