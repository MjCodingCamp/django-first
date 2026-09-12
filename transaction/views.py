from rest_framework.decorators import APIView
from .serializers import TransactionSerializer
from django.http import JsonResponse

class TransactionView(APIView):

    def post(self, request):
        data = request.data 
        serialized_data = TransactionSerializer(data = data)

        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                'status_code': 200,
                'message': 'Transaction has been recorded successfully',
                'data': serialized_data.data
            })
        else: 
            return JsonResponse({
                'status_code': 404,
                'message': 'Invalid Transaction',
                'data': serialized_data.errors
            })