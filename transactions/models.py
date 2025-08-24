from django.db import models
from users.models import CustomUser

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])
    date_created = models.DateTimeField(auto_now_add=True)
