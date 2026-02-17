import json
from reader import Reader

class JSONReader(Reader):
    def load(self):
        with open(self.path, "r", encoding="utf-8") as fd:
            self.data = json.load(fd)

        if not isinstance(self.data, list):
            raise ValueError("JSON must be a list")

    def save(self, destination):
        with open(destination, "w", encoding="utf-8") as fd:
            json.dump(self.data, fd, indent=4)