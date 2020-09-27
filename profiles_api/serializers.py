from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        # we only use password while creating user so we made it write only by extra keyword args
        # so we are restricting to send password through API
        extra_kwargs = {
            'password': {
                'write_only': True,
                # This is for only web interface of API not for application/json type inputs
                # It shows password chars as *
                'style': {'input_type': 'password'}
            }
        }

    # Overriding the existing ModelSerializer function to create user and store the password in hash format
    # if we do not override it and then it will store the password in plain text format
    def create(self, validated_data):
        """Create and return a ne user"""

        # Using existing create_user method defined in our UserProfile class
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user