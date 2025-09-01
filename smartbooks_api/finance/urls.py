from rest_framework import routers
from django.urls import path, include
from .views import IncomeViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
