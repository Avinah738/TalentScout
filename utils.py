import json
import os

# File path for simulated storage
DATA_FILE = "candidate_data.json"

# Initialize storage file
def init_storage():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump({"candidates": []}, file)

# Save candidate details
def save_candidate_data(candidate):
    init_storage()
    with open(DATA_FILE, "r+") as file:
        data = json.load(file)
        data["candidates"].append(candidate)
        file.seek(0)
        json.dump(data, file, indent=4)

# Get all stored data
def get_all_candidates():
    init_storage()
    with open(DATA_FILE, "r") as file:
        return json.load(file)["candidates"]
