from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta: 
        model = UserProfile
        fields = '__all__'

    def age_validate(self, data):
        age = data.get('age')
        if age < 12 or age > 60:
            raise serializers.ValidationError('Invalid Age, it must be between 12 to 60 years.')
