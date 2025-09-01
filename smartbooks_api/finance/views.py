from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend

from .models import Income, Expense, Account, Category, Transaction
from .serializers import (
    IncomeSerializer,
    ExpenseSerializer,
    AccountSerializer,
    CategorySerializer,
    TransactionSerializer,
)


# income and expense
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# account and categories
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# transaction
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["account", "category", "transaction_type", "date"]
    search_fields = ["description"]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# report
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def summary_report(request):
    user = request.user

    income_total = Income.objects.filter(user=user).aggregate(total=Sum("amount"))["total"] or 0
    expense_total = Expense.objects.filter(user=user).aggregate(total=Sum("amount"))["total"] or 0
    balance = income_total - expense_total

    
    income_by_category = (
        Income.objects.filter(user=user)
        .values("category__name")
        .annotate(total=Sum("amount"))
    )
    expense_by_category = (
        Expense.objects.filter(user=user)
        .values("category__name")
        .annotate(total=Sum("amount"))
    )

    data = {
        "income_total": income_total,
        "expense_total": expense_total,
        "balance": balance,
        "income_by_category": list(income_by_category),
        "expense_by_category": list(expense_by_category),
    }
    return Response(data)
