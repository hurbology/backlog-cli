from backlog import storage
from datetime import datetime

def add_games(titles, platform):
    games = storage.load() # load the backlog from the .JSON file

    # Calculate ID: find max ID or start at 0
    current_ids = [game["id"] for game in games]
    next_id = max(current_ids, default=-1) + 1

    for title in titles:
        new_game = {
            "id": next_id,
            "title": title,
            "platform": platform,
            "status": "backlog",
            "added": datetime.now().isoformat(),
            "completed": None,
        }
        games.append(new_game)
        next_id += 1
    
    storage.save(games) # saves the updated backlog to the .JSON file
    print(f"Added {len(titles)} game(s) to your backlog.")

def list_games(status=None):
    games = storage.load() # load the backlog from the .JSON file

    if status:
        games = [game for game in games if game["status"] == status]
    
    for game in games:
        print(f"ID: {game['id']}, Title: {game['title']}, Platform: {game['platform']}, Status: {game['status']}")

def update_game_status(game_id, status):
    games = storage.load()
    for game in games:
        if game["id"] == game_id:
            game["status"] = status
            if status == "completed":
                game["completed"] = datetime.now().isoformat()
            storage.save(games)
            print(f"Updated {game_id} to {status}.")
            return
    print(f"Game ID not found.")

def roll_game():
    pass