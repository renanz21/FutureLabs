from ast import literal_eval

def load_data(file_path, default):
    try:
        with open(file_path, "r") as f:
            content = f.read()
            return literal_eval(content)
    except(FileNotFoundError, ValueError, SyntaxError):
        return default

def save_data(file_path, data):
    try:
        with open(file_path, "w") as f:
            f.write(repr(data))
    except OSError:
        print(f"Could not save data on {file_path}")