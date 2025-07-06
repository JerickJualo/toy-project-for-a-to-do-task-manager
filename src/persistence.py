"""
persistence.py

Handles saving and loading persistent data for the To-Do Task Manager.
This module ensures all user accounts and their tasks are written to and read from disk,
allowing the application to retain state across sessions.

Data is serialized to JSON and stored in 'data.json'. The structure includes:
- A list of serialized account dictionaries.
- A list of serialized task dictionaries.
"""

import json
from pathlib import Path
from classes_functs import Account
from tasks import Task

# Path to the JSON file where data is persisted
DATA_FILE = Path("data.json")

def save_data():
    """
    Save all accounts and tasks to a JSON file atomically.

    This function serializes all current instances of Account and Task
    into a structured JSON object and writes it to 'data.json'.
    A temporary file is written first and then renamed to avoid data loss
    in case of an interruption.

    Structure:
    {
        "accounts": [...],
        "tasks": [...]
    }"""


    payload = {
        "accounts": [acct.to_dict() for acct in Account.ALL_ACC],
        "tasks":    [task.to_dict() for task in Task.ALL_TASKS],
    }
    tmp = DATA_FILE.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    tmp.replace(DATA_FILE)



def load_data():
    """
    Load all accounts and tasks from the JSON file (if it exists).

    This function attempts to read 'data.json' and deserialize its contents
    into Account and Task objects. If the file is missing or empty, nothing
    is loaded. If the file is malformed, a warning is printed and loading is skipped.

    Reconstructed accounts are added to the Account registries.
    Tasks are reconstructed and also attached to their respective owner accounts.
    """
    if not DATA_FILE.exists():
        return
    
    text = DATA_FILE.read_text(encoding="utf-8").strip()
    
    if not text:
        # empty file → treat as no data
        return

    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        print("Warning: data.json is corrupted or not valid JSON—starting fresh.")
        return


    with DATA_FILE.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    # First recreate accounts
    for acct_data in payload.get("accounts", []):
        acct = Account.from_dict(acct_data)
        # Account.from_dict should append itself into ALL_ACC, LIST_ACC_ID, etc.

    # Then recreate tasks and attach to owners
    for task_data in payload.get("tasks", []):
        task = Task.from_dict(task_data)
        # Task.from_dict should append to ALL_TASKS, LIST_TASK_ID, NO_TASKS
        # Now also attach to account.tasks:
        owner = next((a for a in Account.ALL_ACC if a.acc_id == task.owner_id), None)
        if owner:
            owner.tasks[task.task_id] = task
