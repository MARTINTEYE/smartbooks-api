# finance/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename="income")
router.register(r'expenses', ExpenseViewSet, basename="expense")

urlpatterns = router.urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("finance.urls")), 
]
