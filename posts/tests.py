from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="Test post")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        test_string = str(post.text)

        self.assertEqual(test_string, "Test post")


class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(text="Test post")

    def test_view_states(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        print(reverse('home'))
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'home.html')