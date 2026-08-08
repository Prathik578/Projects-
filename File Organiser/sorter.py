import os
from pathlib import Path
import shutil
from datetime import datetime

from config import EXCLUDED_DIRECTORIES, FILE_TYPES, UNKNOWN_FOLDER, LOG_FILE, COLLISION_FORMAT

def log_action(action, source, destination):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {action}: {source} → {destination}\n")

def sort_folder(folder, dry_run):

    stats = {
        "scanned": 0,
        "moved": 0,
        "collisions": 0,
        "errors": 0,
        "categories": {},
    }

    items = []

    output_folders = set(FILE_TYPES.values())
    output_folders.add(UNKNOWN_FOLDER)

    for root, directories, files in os.walk(folder):

        directories[:] = [
            directory
            for directory in directories
            if directory not in output_folders
            and directory not in EXCLUDED_DIRECTORIES
        ]

        for file in files:
            items.append(Path(root) / file)
            stats["scanned"] += 1

    for item in items:
        extension = item.suffix.lower()
        folder_name = FILE_TYPES.get(extension, UNKNOWN_FOLDER)

        stats["categories"][folder_name] = (
            stats["categories"].get(folder_name, 0) + 1
        )

        destination_folder = folder / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / item.name

        if destination.exists():
            stats["collisions"] += 1

        destination = get_unique_destination(destination)

        if dry_run:
            print(f"Would move: {item} → {destination}")
        else:
            shutil.move(item, destination)
            stats["moved"] += 1
            log_action("MOVED", item, destination)
            print(f"Moved: {item.name} → {folder_name}/")

    return stats

def get_unique_destination(destination):

    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = COLLISION_FORMAT.format(
            stem=destination.stem,
            counter=counter,
            suffix=destination.suffix
        )
        new_destination = destination.parent / new_name
        if not new_destination.exists():
            return new_destination
        counter += 1

