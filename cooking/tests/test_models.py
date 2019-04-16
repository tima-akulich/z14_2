import random

from django.test import TestCase

from cooking.models import Recipe, RecipeReaction, User
from django.conf import settings


class TestModels(TestCase):
    def test_ok(self):
        pass

    def test_recipe_methods(self):
        recipe = Recipe.objects.create(
            title='Test title',
            text='Test text'
        )
        user = User.objects.create(
            username='test_user'
        )
        self.assertEqual(str(recipe), 'None - Test title')

        self.assertEqual(
            recipe.get_absolute_url(),
            f'/{settings.LANGUAGE_CODE}/recipe/{recipe.id}/'
        )

        num = random.randint(1, 1000)
        reactions = [RecipeReaction(
            user=user,
            status=RecipeReaction.LIKE,
            recipe=recipe)
        ] * num
        RecipeReaction.objects.bulk_create(reactions)
        self.assertEqual(num, recipe.likes)
