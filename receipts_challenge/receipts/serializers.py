from receipts.models import Receipt
from rest_framework import serializers


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id', 'retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']