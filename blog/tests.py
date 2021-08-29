from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='User_1', email='user@gmail.com', password='user')
        self.post = Post.create(title='Test', text='some text', body='somebody', author=self.user)

    def test_post_content(self):
        self.assertEqual(str(self.post.title), 'Test')
        self.assertEqual(str(self.post.body), 'somebody')

    def test_post_list_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "nice")
        self.assertTemplateUsed(resp, 'home.html')

    def test_post_detail(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/100/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 400)

        self.assertTemplateUsed(resp, 'post_detail.html')
