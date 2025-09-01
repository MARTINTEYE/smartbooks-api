from django.contrib import admin
from .models import Account, Category, Income, Expense

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "account_type", "balance", "user")
    list_filter = ("account_type",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category_type", "user")
    list_filter = ("category_type",)
    search_fields = ("name",)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")
