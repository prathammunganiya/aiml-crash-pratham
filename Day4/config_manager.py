import json


def save_config(data: dict, filename: str):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value):
    data = load_config(filename)
    data[key] = value
    save_config(data, filename)


config = {
    "model": "GPT",
    "learning_rate": 0.001,
    "epochs": 10
}

save_config(config, "config.json")
update_config("config.json", "epochs", 20)

# json.dump() writes JSON to a file.
# json.dumps() converts JSON into a string.