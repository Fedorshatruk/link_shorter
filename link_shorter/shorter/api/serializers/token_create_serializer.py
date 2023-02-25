from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shorter.models import Token
from shorter.utils import generate_subpart


class TokenCreateSerializer(serializers.ModelSerializer):
    subpart = serializers.CharField(required=False)

    class Meta:
        model = Token
        fields = (
            'full_url',
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
