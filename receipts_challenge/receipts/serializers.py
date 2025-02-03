from receipts.models import Item, Receipt
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price']


class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Receipt
        fields = ['id', 'retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']