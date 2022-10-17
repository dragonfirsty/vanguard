import ipdb
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class TraitDataMixin:
    def create(self, request, *args, **kwargs):

        initial_data = self.get(request).data
        data = []

        for line in initial_data:

            data_string = {}
            data_string.update({"uuid": line["uuid"]})
            data_string.update({"type": line["type"]})
            data_string.update({"date": line["date"]})
            data_string.update({"value": float(line["value"])})
            data_string.update({"cpf": line["cpf"]})
            data_string.update({"card": line["card"]})
            data_string.update({"time": line["time"]})
            data_string.update({"store_owner": line["store_owner"]})
            data_string.update({"store_name": line["store_name"]})
            data.append(data_string)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
