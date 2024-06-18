from django.db import models

# Create your models here.


from django.db import models

class ShareTrade(models.Model):
    TRADE_TYPES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=4, choices=TRADE_TYPES)
    user_id = models.IntegerField()
    symbol = models.CharField(max_length=5)
    shares = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.BigIntegerField()

