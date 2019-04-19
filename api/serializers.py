from rest_framework import serializers

from cooking.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title'
        )


class RecipeDetailsSerializer(RecipeSerializer):
    recipe_image = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + (
            'text',
            'level',
            'recipe_image',
            'likes_count'
        )

    def get_recipe_image(self, obj):
        return obj.get_image

    def get_likes_count(self, obj):
        return getattr(obj, 'likes_count', None)
