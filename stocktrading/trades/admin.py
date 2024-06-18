from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *

@admin.register(ShareTrade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'user_id', 'symbol', 'shares', 'price', 'timestamp')
    list_filter = ('type', 'user_id', 'symbol')
    search_fields = ('symbol', 'user_id')
    ordering = ('id',)
