import os

class Reader:
    def __init__(self, path):
        self.path = path
        self.data = []

    def load(self):
        raise NotImplemented

    def save(self, destination):
        raise NotImplemented

    def display(self):
        print("\nCurrent location:")
        for row in self.data:
            print(row)
        print()

    def apply_changes(self, changes):

        for change in changes:
            parsed = parse_change(change)
            if parsed is None:
                print(f"Invalid change: {change}")
                continue

            col, row, value = parsed

            if row < 0 or row >= len(self.data):
                print(f"Change skipped, row out of range: {change}")
                continue

            if row < 0 or row >= len(self.data[row]):
                print(f"Change skipped, column out of range: {change}")
                continue

            self.data[row][col] = value

        print("Content modified")

def list_files_in_dir(path):
    dir = os.path.dirname(path) or "."
    try:
        files = os.listdir(dir)
        print(f"Files in '{os.path.abspath(dir)}")
        for f in files:
            print(" -", f)
    except OSError:
        print("Unable to print content")

def parse_change(change):
    #EV1
    parts = change.split(',', 2)
    if len(parts) != 3:
        return None

    try:
        col = int(parts[0])
        row = int(parts[1])
        value = parts[2]
    except ValueError:
        return None

    return col, row, value