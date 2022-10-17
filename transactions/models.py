import uuid

from django.db import models


class TransactionsChoices(models.TextChoices):
    DEBITO = "Debito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Credito"
    EMPRESTIMO = "Recebimento Emprestimo"
    VENDAS = "Vendas"
    TED = "Recebimento TED"
    DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"


class Transactions(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=30, choices=TransactionsChoices.choices)
    date = models.DateField()
    value = models.DecimalField(decimal_places=2,max_digits=30)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=30)
    time = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)