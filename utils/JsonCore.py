import json


def read_json(path):
    with open(path) as json_file:
        return json.load(json_file)


def write_to_json(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=2)

