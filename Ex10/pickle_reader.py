import pickle
from reader import Reader

class PickleReader(Reader):
    def load(self):
        with open(self.path, "rb") as fd:
            self.data = pickle.load(fd)

        if not isinstance(self.data, list):
            raise ValueError("Pickle must contain a list")

    def save(self, destination):
        with open(destination, "wb") as fd:
            pickle.dump(self.data, fd)