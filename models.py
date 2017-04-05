from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Transaction(models.Model):
	transaction_type=(
		('Deposit' , 'D'),
		('Withdraw' , 'W'),
		)
	amount=models.IntegerField()
	date_of_transaction=models.DateTimeField()
	transaction_type=models.CharField(max_length= 20)
	cost=models.IntegerField()
	phonenumber=PhoneNumberField(max_length=10)