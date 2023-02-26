from django.db.models import F, Value
from django.db.models.functions import Concat

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from shorter.api.mixins import RedisCreateModelMixin, RedisDestroyModelMixin, RedisUpdateModelMixin
from shorter.api.serializers import TokenCreateSerializer, TokenListSerializer
from shorter.models import Token


class TokenViewSet(
    RedisCreateModelMixin,
    RedisUpdateModelMixin,
    mixins.ListModelMixin,
    RedisDestroyModelMixin,
    GenericViewSet,
):
    queryset = Token.objects.all()
    serializer_class = TokenCreateSerializer
    lookup_field = 'subpart'

    def _get_current_site(self):
        return self.request.build_absolute_uri('/')

    def get_queryset(self):

        queryset = super().get_queryset().filter(owner=self.request.owner)
        if self.action == 'list':
            queryset = queryset.annotate(
                short_link=Concat(
                    Value(self._get_current_site()),
                    F('subpart'),
                )
            )
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TokenListSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context: dict = super().get_serializer_context()
        context['owner'] = self.request.owner
        return context
