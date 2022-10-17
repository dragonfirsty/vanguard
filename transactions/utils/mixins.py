from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class TraitDataMixin:
    def create(self, request, *args, **kwargs):
        types = [
            "Debito",
            "Boleto",
            "Financiamento",
            "Credito",
            "Recebimento Emprestimo",
            "Vendas",
            "Recebimento TED",
            "Recebimento DOC",
            "Aluguel",
        ]
        data_parse = []
        for line in request.data:
            i = 0
            condition = True
            while condition:
                if line["type"] == str(i + 1):
                    line["type"] = types[i]
                    condition = False
                else:
                    i += 1
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
