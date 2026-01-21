import sys
import os
import csv

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

def main():
    if len(sys.argv) < 3:
        print("Example of use of script - python <path> <source> <destination> <change1> <change2>") # python Ex7.py csv_file.csv csv_file_mod.csv 0,0,piano 3,1,mug
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
        with open(source, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
    except Exception as e:
        print("Error reading CSV file")
        sys.exit(1)

    if not data:
        print("CSV file is empty")

    for change in changes:
        parsed = parse_change(change)
        if parsed is None:
            print("Invalid change format: expected <row> <col> <value>\n")
            continue

        col, row, value = parsed

        if row < 0 or row >=len(data):
            print("Change skipped, row does not exist")
            continue
        if col < 0 or col >=len(data[row]):
            print("Change skipped, column does not exist")
            continue

        data[row][col] = value

    print("Content modified")

    try:
        with open(destination, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    except Exception as e:
        print("Error writing CSV file")
        sys.exit(1)

if __name__ == "__main__":
    main()