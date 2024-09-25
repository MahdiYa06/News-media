from django.db import models
from utils.base import TimeStampModel
from django.db.models.functions import TruncDate



class Subscription(TimeStampModel):
    user = models.OneToOneField("user.User", verbose_name="User", on_delete=models.CASCADE, related_name='sub')
    trial_start_date = models.DateTimeField("Trial start date")
    trial_end_date = models.DateTimeField("Trial start date")
    
    
    def __str__(self) -> str:
        return self.user
    
    
    class Meta:
        db_table = 'Subscriptions'
    
    
    
class Payment(TimeStampModel):
    subscription = models.ForeignKey("subscriptify.Subscription", verbose_name="Subscription", on_delete=models.PROTECT, related_name='payments')
    success = models.BooleanField("succeeded")
    tracking_id = models.CharField("Payment Gateway Tracking ID", max_length=150)
    status = models.CharField("Order Status", max_length=150)
    
    
    def __str__(self) -> str:
        return f'{self.subscription.user}({self.status})'
    
    
    
    class Meta:
        db_table = "Payments"
        indexes = [models.Index(TruncDate("created_at"), "created_at", name="payment_created_at_date_idx")]
    