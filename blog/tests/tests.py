from django.test import TestCase
from blog.models import Post

class PostModelTests(TestCase):
    def test_is_empty(self):
        article = Post.objects.all()
        self.assertEqual(article.count(), 0)