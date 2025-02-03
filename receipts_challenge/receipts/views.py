from django.http import Http404
from receipts.models import Receipt
from receipts.serializers import ReceiptSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ReceiptProcess(APIView):
    def post(self, request, format=None):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

class ReceiptPoints(APIView):
    def get_object(self, pk):
        try:
            return Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        receipt = self.get_object(pk)
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data) #change later