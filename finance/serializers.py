# finance/serializers.py
from rest_framework import serializers
from .models import Income, Expense

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "source", "amount", "description", "date", "created_at", "updated_at"]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "category", "amount", "description", "date", "created_at", "updated_at"]
