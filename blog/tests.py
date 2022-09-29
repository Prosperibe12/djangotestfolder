from django.test import TestCase
from blog.models import Post


# Create your tests here.
class BlogModelTest(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
