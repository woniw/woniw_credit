import json
import os

# Get the directory where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_json(filename):
    """Load JSON data from a file located relative to the script's directory."""
    filepath = os.path.join(BASE_DIR, filename)
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[!] {filename} not found. Returning empty dict.")
        return {}
    except json.JSONDecodeError:
        print(f"[!] Error decoding JSON from {filename}. Returning empty dict.")
        return {}

def save_json(filename, data):
    """Save Python object as JSON to a file located relative to the script's directory."""
    filepath = os.path.join(BASE_DIR, filename)
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Data saved to {filename}")
    except Exception as e:
        print(f"[!] Error saving data to {filename}: {e}")



