from rest_framework import serializers

from shorter.models import Token


class TokenListSerializer(serializers.ModelSerializer):
    short_link = serializers.URLField()

    class Meta:
        model = Token
        fields = [
            'full_url',
            'request_count',
            'short_link',
            'subpart',
        ]
