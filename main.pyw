# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime
from send2trash import send2trash

# get folder
SCREENSHOT_FOLDER_PATH = os.path.expanduser(r"C:\Users\damne\OneDrive\Pictures\Zrzuty ekranu")
SYSTEM_FILES = ["desktop.ini", "photothumb.db", "thumbs.db", "~$"]
LOG_FILE = os.path.join(os.path.dirname(__file__), "delete_log.txt")

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: {msg}\n")

def delete_files():
    print("Start delete_files()")

    any_old_files = False
    deleted_count = 0

    for file in os.listdir(SCREENSHOT_FOLDER_PATH):
        filepath = os.path.join(SCREENSHOT_FOLDER_PATH, file)

        if os.path.isdir(filepath):
            continue

        if any(file.lower().startswith(s) or file.lower() == s for s in SYSTEM_FILES):
            continue

        mod_time = os.path.getmtime(filepath)
        now = time.time()
        file_age = now - mod_time
        five_days_in_seconds = 5 * 24 * 60 * 60

        if file_age > five_days_in_seconds:
            print(f"{file} jest starszy niż 5 dni ({file_age / 86400:.2f} dni)")
            send2trash(filepath)
            deleted_count += 1
            print(f"{file} został usunięty")
            any_old_files = True

    if not any_old_files:
        print("Nie ma plików starszych niż 5 dni")
        log("Nie znaleziono plików starszych niż 5 dni")
    else:
        print(f"Usunięto {deleted_count} plików starszych niż 5 dni")
        log(f"Usunięto {deleted_count} plików starszych niż 5 dni")




if __name__ == "__main__":
    delete_files()