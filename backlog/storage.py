import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".backlog.json"

def load(path: Path = DEFAULT_PATH):
    try:
        return json.loads(path.read_text()) # returns the backlog as a list of dicts
    except FileNotFoundError:
        return [] # on first run backlog.json file doesn't exist, instead of crashing, return an empty list

def save(games, path: Path = DEFAULT_PATH):
    path.write_text(json.dumps(games, indent=2)) # turns the python list of dicts into a readable json file and saves it to the default path
