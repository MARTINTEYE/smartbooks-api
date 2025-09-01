from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Account, Category, Income, Expense


class IncomeForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        if category and category.category_type != "income":
            raise ValidationError("Selected category must be of type 'Income'.")
        return cleaned_data


class ExpenseForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        if category and category.category_type != "expense":
            raise ValidationError("Selected category must be of type 'Expense'.")
        return cleaned_data


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
    form = IncomeForm
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseForm
    list_display = ("id", "amount", "date", "account", "category", "user")
    list_filter = ("date", "account", "category")
