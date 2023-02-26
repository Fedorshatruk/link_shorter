from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shorter.models import Token
from shorter.utils import generate_subpart


class TokenCreateSerializer(serializers.ModelSerializer):
    subpart = serializers.CharField(required=False)
    request_count = serializers.IntegerField(read_only=True)
    short_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Token
        fields = (
            'full_url',
            'request_count',
            'short_link',
            'subpart',
        )

    def validate_subpart(self, value):
        if Token.objects.filter(subpart=value).exists():
            raise ValidationError('with this subpart already exists.')
        return value

    def validate(self, attrs):
        if not attrs.get('subpart'):
            attrs['subpart'] = generate_subpart()
        attrs['owner'] = self.context.get('owner')
        return attrs

    def get_short_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/{obj.subpart}')