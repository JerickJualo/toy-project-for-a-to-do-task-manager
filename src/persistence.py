# persistence.py
import json
from pathlib import Path
from classes_functs import Account
from tasks import Task

DATA_FILE = Path("data.json")

def save_data():
    """Serialize all accounts & tasks to disk atomically."""
    payload = {
        "accounts": [acct.to_dict() for acct in Account.ALL_ACC],
        "tasks":    [task.to_dict() for task in Task.ALL_TASKS],
    }
    tmp = DATA_FILE.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    tmp.replace(DATA_FILE)



def load_data():
    """Load accounts & tasks from disk (if present)."""
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
