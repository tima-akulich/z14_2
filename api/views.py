from django.db.models import Case, IntegerField
from django.db.models import Count
from django.db.models import When
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    get_object_or_404, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import RecipeSerializer, RecipeDetailsSerializer
from cooking.models import Recipe


@api_view(['GET'])
def my_first_api_view(request, *args, **kwargs):
    return Response(data={
        'status': 'ok'
    }, status=202)


class RecipeRetrieveView(RetrieveAPIView, DestroyAPIView):
    serializer_class = RecipeDetailsSerializer

    def get_object(self):
        return get_object_or_404(Recipe, pk=self.kwargs['pk'])


class RecipeListView(ListAPIView, CreateAPIView):
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer

    def get_queryset(self):
        annotate_kwargs = {
            'likes_count': Count(
                Case(
                    When(
                        reactions__status='like',
                        then=1,
                    ),
                    output_field=IntegerField()
                )
            )
        }
        if self.request.user.is_authenticated:
            annotate_kwargs['liked'] = Count(
                Case(
                    When(
                        reactions__status='like',
                        reactions__user=self.request.user,
                        then=1,
                    ),
                    output_field=IntegerField()
                )
            )

        queryset = super().get_queryset().annotate(**annotate_kwargs)
        return queryset


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        print(self.request.user)
        return super().get_serializer_class()