import uuid

from django.db import models


class TransactionsChoices(models.TextChoices):
    DEBITO = "Débito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Crédito"
    EMPRESTIMO = "Recebimento Empréstimo"
    VENDAS = "Vendas"
    TED = "Recebimento TED"
    DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"


class Transactions(models.Model):
    uuid: models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=30, choices=TransactionsChoices.choices)
    created_at = models.DateField(auto_now_add=True)
    value = models.IntegerField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.IntegerField(max_length=12)
    time = models.DateTimeField(auto_now_add=True)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)