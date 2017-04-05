from django.contrib import admin
from mpesa.models import Transaction

# Register your models here. 
class TransactionAdmin(admin.ModelAdmin):
	list_display=('phonenumber','transaction_type','date_of_transaction','amount','cost')
admin.site.register(Transaction,TransactionAdmin)