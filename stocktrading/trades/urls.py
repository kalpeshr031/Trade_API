from django.urls import path
from .views import TradeListCreateView, TradeDetailView

urlpatterns = [
    path('trades/', TradeListCreateView.as_view(), name='list-create'),
    path('trades/<int:pk>/', TradeDetailView.as_view(), name='trade-detail'),
]

