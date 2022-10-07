from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

from .serializers import TransactionsSerializer
from .models import Transactions

class TransactionsView(ListCreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()


class TransactionsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()