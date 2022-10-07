import numbers
import ujson as json



def read_data(path: str) -> list[dict]:
    try:
        with open(path, "r") as database:
            json_data = json.load(database)
    except (json.JSONDecodeError, FileNotFoundError, FileExistsError):
        return []
    return json_data


def write_data(path: str):
    data = []
    fields = ["type", "date", "value", "cpf", "card", "date", "store_name","owner_store"]
    with open(path) as fh:
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
            data_string.update({fields[7]: description[0][62:81]})
            data.append(data_string)
        return data   