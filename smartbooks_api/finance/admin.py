from django.contrib import admin
from .models import Account, Category, Income, Expense

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "balance", "user")
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    search_fields = ("name",)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")
