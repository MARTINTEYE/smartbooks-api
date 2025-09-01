from rest_framework import routers
from django.urls import path, include
from .views import IncomeViewSet, ExpenseViewSet, TransactionViewSet
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]

router = DefaultRouter()


urlpatterns += router.urls
