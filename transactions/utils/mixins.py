import json
import ipdb

class TraitDataMixin:
    def create(self, request, *args, **kwargs):
        
        # test = request.FILES['file'].read()
        # print("-" * 100)
        # print("-" * 100)
        # print("123413")
        # print("-" * 100)
        data = []
        fields = [
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "time",
            "owner_store",
            "store_name",
        ]
        with open(request.FILE) as fh:
            for line in fh:
                description = line.strip().split(None, 0)
                data_string = {}
                data_string.update({fields[0]: description[0][0:1]})
                data_string.update({fields[1]: description[0][1:9]})
                data_string.update({fields[2]: description[0][9:19]})
                data_string.update({fields[3]: description[0][19:30]})
                data_string.update({fields[4]: description[0][30:42]})
                data_string.update({fields[5]: description[0][42:48]})
                data_string.update({fields[6]: description[0][48:62]})
                data_string.update({fields[7]: description[0][62:80]})
                data.append(data_string)
            print(data)
            return data
