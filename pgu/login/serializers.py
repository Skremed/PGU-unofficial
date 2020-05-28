from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        fields = ('user', 'password')
