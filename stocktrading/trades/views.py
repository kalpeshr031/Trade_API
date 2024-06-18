from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.exceptions import MethodNotAllowed, NotFound
from .models import ShareTrade
from .serializers import TradeSerializer


class TradeListCreateView(ListCreateAPIView):
    queryset = ShareTrade.objects.all()
    # print("-----queryset")
    serializer_class = TradeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        trade_type = self.request.query_params.get('type')
        user_id = self.request.query_params.get('user_id')

        if trade_type:
            queryset = queryset.filter(type=trade_type)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        
        return queryset.order_by('id')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TradeDetailView(RetrieveAPIView):
    queryset = ShareTrade.objects.all()
    serializer_class = TradeSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE method is not allowed")

    def put(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT method is not allowed")

    def patch(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH method is not allowed")
