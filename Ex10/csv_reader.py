import csv
from reader import Reader

class CSVReader(Reader):
    def load(self):
        with open(self.path, newline="", encoding="utf-8") as fd:
            reader = csv.reader(fd)
            self.data = list(reader)

    def save(self, destination):
        with open(destination, "w", newline="", encoding="utf-8") as fd:
            writer = csv.writer(fd)
            writer.writerows(self.data)