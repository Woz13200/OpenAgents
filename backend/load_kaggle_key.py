import os
import json

def setup_kaggle_key():
    cfg = {
        "username": os.getenv("KAGGLE_USERNAME"),
        "key": os.getenv("KAGGLE_KEY")
    }
    os.makedirs(os.path.expanduser("~/.config/kaggle"), exist_ok=True)
    with open(os.path.expanduser("~/.config/kaggle/kaggle.json"), "w") as f:
        json.dump(cfg, f)

setup_kaggle_key()
