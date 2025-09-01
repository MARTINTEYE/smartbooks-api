from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IncomeViewSet,
    ExpenseViewSet,
    AccountViewSet,
    CategoryViewSet,
    TransactionViewSet,
    summary_report,
)

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename='income')
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
    path('reports/summary/', summary_report, name='summary-report'),
]
