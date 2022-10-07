import ujson as json

from utils.json_handler import write_data

FILEPATH = "test.txt"

if __name__ == "__main__":
    test = write_data(FILEPATH)
    final = json.dumps(test, indent=2)
    
    print(test)
