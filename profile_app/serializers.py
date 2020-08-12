from rest_framework import serializers
from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    '''Serializers a name field for testing APIView'''
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
