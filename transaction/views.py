from rest_framework.decorators import APIView
from .serializers import TransactionSerializer
from django.http import JsonResponse
from .models import Transaction

class TransactionView(APIView):

    def get(self, request):
        user_id = request.query_params.get('user_id')

        if not user_id:
            return JsonResponse({
                'status_code': 404,
                'message': 'user_id is required',
                'data': []
            })

        transactions = Transaction.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)

        return JsonResponse({
            'status_code': 200,
            'message': 'Transactions fetched successfully',
            'data': serializer.data
        })
             

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