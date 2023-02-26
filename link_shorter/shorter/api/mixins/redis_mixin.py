from rest_framework import mixins

from shorter.utils import client


class RedisUpdateModelMixin(mixins.UpdateModelMixin):

    def perform_update(self, serializer):
        instance = serializer.save()
        redirect_url = instance.full_url
        subpart = instance.subpart
        client.set(subpart, redirect_url)


class RedisCreateModelMixin(mixins.CreateModelMixin):

    def perform_create(self, serializer):
        instance = serializer.save()
        redirect_url = instance.full_url
        subpart = instance.subpart
        client.set(subpart, redirect_url)


class RedisDestroyModelMixin(mixins.DestroyModelMixin):

    def perform_destroy(self, instance):
        subpart = instance.subpart
        client.delete(subpart)
        instance.delete()

