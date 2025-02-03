from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from receipts.models import Receipt
from receipts.serializers import ReceiptSerializer
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def receipts(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReceiptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def receipt_points(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
    except Receipt.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ReceiptSerializer(receipt)
        return JsonResponse(serializer.data) #change later