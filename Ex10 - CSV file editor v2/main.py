import os
import sys

from csv_reader import CSVReader
from reader import list_files_in_dir
from json_reader import JSONReader
from pickle_reader import PickleReader

def create_reader(path):
    extension = os.path.splitext(path)[1].lower()

    if extension == ".csv":
        return CSVReader(path)
    elif extension == ".json":
        return JSONReader(path)
    elif extension == ".pickle":
        return PickleReader(path)
    else:
        raise ValueError("Invalid file extension")

def main():
    if len(sys.argv) < 3:
        print(
            "Example of use of script - python <path> <source> <destination> <change1> <change2>")  # python main.py csv_file.csv.csv csv_modified.json "0,0,piano" "1,1,mug"
        print("Example of change: <row>,<col>,<value>\n")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.exists(source) or not os.path.isfile(source):
        print("Error, source file does not exist")
        list_files_in_dir(source)
        sys.exit(1)

    try:
        reader = create_reader(source)
        reader.load()
    except Exception as e:
        print("Error reading CSV file")
        sys.exit(1)

    reader.display()
    reader.apply_changes(changes)
    reader.display()

    try:
        dest_reader = create_reader(destination)
        dest_reader.data = reader.data
        dest_reader.save(destination)
    except Exception as e:
        print("Error writing CSV file")
        sys.exit(1)

    print(f"File saved to {destination}")

if __name__ == "__main__":
    main()