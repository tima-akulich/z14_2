from django.test import TestCase
from django.urls import reverse

from cooking.models import User, Recipe


class TestViews(TestCase):
    def test_view(self):
        response = self.client.get(reverse('feed'))
        self.assertTemplateUsed(response, 'recipe_list.html')
        self.assertEqual(response.status_code, 200)
        print(response.context['request'])

    def test_user_feed_view(self):
        response = self.client.get(reverse('user.feed'))
        print(response.status_code)
        print(response.url)
        self.assertNotEqual(response.status_code, 200)

        user = User.objects.create_user(username='test', password='test')
        is_login = self.client.login(username='test', password='test123')
        self.assertFalse(is_login)
        is_login = self.client.login(username='test', password='test')
        self.assertTrue(is_login)

        response = self.client.get(reverse('user.feed'))
        self.assertEqual(response.status_code, 200)

        prev_count = Recipe.objects.filter(author=user).count()

        response = self.client.post(reverse('create'), data={
            'title': 'Title',
            'text': 'text',
            'level': 1
        })

        current_count = Recipe.objects.filter(author=user).count()
        self.assertEqual(current_count - prev_count, 1)
