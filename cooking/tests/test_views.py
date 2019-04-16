from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):
    def test_view(self):
        response = self.client.get(reverse('feed'), HTTP_USER_AGENT='client_agent')
        self.assertTemplateUsed(response, 'recipe_list.html')
        self.assertEqual(response.status_code, 200)
        print(response.context['request'])

    def test_user_feed_view(self):
        # response = self.client.get(reverse('user.feed'))
        # self.assertNotEqual(response.status_code, 200)
        pass

