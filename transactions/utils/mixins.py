from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class TraitDataMixin:
    def create(self, request, *args, **kwargs):

        data_parse = []

        for line in request.data:
            if line["type"] == "1":
                line["type"] = "Debito"
            elif line["type"] == "2":
                line["type"] = "Boleto"
            elif line["type"] == "3":
                line["type"] = "Financiamento"
            elif line["type"] == "4":
                line["type"] = "Credito"
            elif line["type"] == "5":
                line["type"] = "Recebimento Emprestimo"
            elif line["type"] == "6":
                line["type"] = "Vendas"
            elif line["type"] == "7":
                line["type"] = "Recebimento TED"
            elif line["type"] == "8":
                line["type"] = "Recebimento DOC"
            elif line["type"] == "9":
                line["type"] = "Aluguel"
            line[
                "date"
            ] = f"{line['date'][0:4]}-{line['date'][4:6]}-{line['date'][6:8]}"
            line["value"] = int(line["value"])
            line["value"] = line["value"] / 100
            line["store_owner"] = line["store_owner"].strip()
            line["store_name"] = line["store_name"].strip()
            line[
                "time"
            ] = f"{line['time'][0:2]}:{line['time'][2:4]}:{line['time'][4:6]}"
            data_parse.append(line)

        serializer = self.get_serializer(data=data_parse, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
