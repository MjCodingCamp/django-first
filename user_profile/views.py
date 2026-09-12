from rest_framework.decorators import APIView
from django.http import JsonResponse
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileView(APIView):

    def get(self, request):
        user_id = request.query_params.get('user_id')

        if not user_id:
            return JsonResponse({
                'status_code': 404,
                'message': 'user_id is required',
                'data': None
            })

        try:
            user = UserProfile.objects.get(user_id=user_id)
            serialized_data = UserProfileSerializer(user)
            return JsonResponse({
                'status_code': 200,
                'message': 'User fetched successfully',
                'data': serialized_data.data
            })

        except Exception as error:
            return JsonResponse({
                'status_code': 500,
                'message': str(error),
                'data': None
            })


    def post(self, request):
        data = request.data
        serialized_data = UserProfileSerializer(data = data)

        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                'status_code': 200,
                'message': 'User record has been saved'
            })
        else: 
            return JsonResponse({
                'status_code': 400,
                'message': 'Invalid request fields',
                'error': serialized_data.errors
            })
