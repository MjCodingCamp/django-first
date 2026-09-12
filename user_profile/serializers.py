from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta: 
        model = UserProfile
        fields = '__all__'

    def validate_age(self, value):
        if value < 12 or value > 60:
            raise serializers.ValidationError(
                'Invalid age. It must be between 12 and 60 years.'
            )
        return value
