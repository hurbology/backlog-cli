import json
from pathlib import Path

BASE_DIR = Path.home() / ".backlog-tracker-cli"
DEFAULT_PATH = BASE_DIR / ".backlog.json"

_is_initialized = False

def _bootstrap():
    global _is_initialized

    if _is_initialized:
        return
    
    # Initialize the storage directory if it doesn't exist
    if not BASE_DIR.exists():
        BASE_DIR.mkdir(parents=True)
        print(f"Created storage directory '.backlog-tracker-cli' at {BASE_DIR}")
    
    _is_initialized = True
    

def load(path: Path = DEFAULT_PATH):
    try:
        return json.loads(path.read_text()) # returns the backlog as a list of dicts
    except FileNotFoundError:
        return [] # on first run backlog.json file doesn't exist, instead of crashing, return an empty list

def save(games, path: Path = DEFAULT_PATH):
    _bootstrap() # Initialize the storage directory if it doesn't exist then becomes a no-op on subsequent calls

    is_new_file = not path.exists() 
    path.write_text(json.dumps(games, indent=2)) # turns the python list of dicts into a readable json file and saves it to the default path

    if is_new_file:
        print(f"Created backlog.json file at {path}")
