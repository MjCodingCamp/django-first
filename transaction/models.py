from django.db import models
from user_profile.models import UserProfile

class Transaction(models.Model):
    status_enum = [
        ('failed', 'Failed'),
        ('success', 'Success'),
        ('pending', 'Pending')
    ]
    method_enum = [
        ('upi', 'Upi'),
        ('card', 'Card'),
        ('netbanking', 'Net Banking')        
    ]

    transaction_id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    transaction_date = models.DateField(auto_now_add=True)
    transaction_status = models.CharField(
        default='success',  
        choices=status_enum
    )
    transaction_method = models.CharField(
        default='upi',  
        choices=method_enum
    )
    user_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
        