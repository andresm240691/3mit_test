from rest_framework import serializers
from .models import BriefCase


class BriefCaseSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.coin.name

    def get_price(self, obj):
        return obj.coin.price

    class Meta:
        model = BriefCase
        fields = [
            'id',
            'total_quantity',
            'average_purchase',
            'trend',
            'price',
            'name',
            'price'
        ]