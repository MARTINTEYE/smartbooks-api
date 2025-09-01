from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Account(models.Model):
    ACCOUNT_TYPES = (
        ("cash", "Cash"),
        ("bank", "Bank"),
        ("mobile_money", "Mobile Money"),
        ("other", "Other"),
    )

    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default="cash")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"


class Category(models.Model):
    CATEGORY_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES, default="expense")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def clean(self):
        if self.category.category_type != "income":
            raise ValidationError("Category must be of type 'Income' for Income records.")

    def __str__(self):
        return f"Income: {self.amount} on {self.date}"


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def clean(self):
        if self.category.category_type != "expense":
            raise ValidationError("Category must be of type 'Expense' for Expense records.")

    def __str__(self):
        return f"Expense: {self.amount} on {self.date}"
