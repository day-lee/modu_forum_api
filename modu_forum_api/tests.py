from django.test import TestCase
from modu_forum_api.models import Post, Comment
from django.contrib.auth.models import User

"""
To run a test, type command below
coverage run --omit='*/venv/*' manage.py test
"""

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Setup a dummy data which can be destroyed after the test
        Note that likes is related as ManytoMany relations to Post
        """
        #User
        testuser1 = User.objects.create_user(
                    username='test_user1',
                    password='123456789')
        testuser1.save()

        #Post
        test_post = Post.objects.create(
                    title='Post Title',
                    excerpt='Post Excerpt',
                    content='Post Content',
                    published='2021-07-21 10:30:00+00:00',
                    author_id=1)
        test_post.likes.set([1])
        test_post.save()

        #Comment
        test_comment = Comment.objects.create(
                    post_id=1,
                    name='Anyone',
                    content='Comment Content',
                    published='2021-07-22 10:30:00+00:00')
        test_comment.save()

    def test_blog_content(self):
        """
        Dummy object Post defined above will be returned as queryset(Post.object.get(id=1)) on the left side
        is compared to expected data content(right side)
        :return: OK or FAILED
        """
        post = Post.objects.get(id=1)
        likes = User.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        published = f'{post.published}'
        likes = post.likes.count()
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(published, '2021-07-21 10:30:00+00:00')
        self.assertEqual(likes, 1)
        self.assertEqual(str(post), "Post Title | test_user1")

    def test_comment_content(self):
        """
        Dummy object Post defined above will be returned as queryset(Post.object.get(id=1)) on the left side
        is compared to expected data content(right side)
        :return: OK or FAILED
        """
        comment = Comment.objects.get(id=1)
        post = f'{comment.post}'
        name = f'{comment.name}'
        content = f'{comment.content}'
        published = f'{comment.published}'
        self.assertEqual(post, 'Post Title | test_user1')
        self.assertEqual(name, 'Anyone')
        self.assertEqual(content, 'Comment Content')
        self.assertEqual(published, '2021-07-22 10:30:00+00:00')
        self.assertEqual(str(comment), "Post Title | Anyone")

