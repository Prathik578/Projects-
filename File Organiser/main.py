import argparse
from pathlib import Path

from sorter import sort_folder


def main():
    parser = argparse.ArgumentParser(
        description="FilePilot - a configurable file organizer"
    )

    parser.add_argument(
        "path",
        help="Folder to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    folder = Path(args.path).expanduser()

    if not folder.exists():
        print(f"Error: folder does not exist: {folder}")
        return

    if not folder.is_dir():
        print(f"Error: not a directory: {folder}")
        return

    try:
       stats = sort_folder(folder, args.dry_run)
       print("\n" + "─" * 30)
       print("FilePilot Summary")
       print("─" * 30)

       print(f"Files scanned:   {stats['scanned']}")

       if args.dry_run:
          print(f"Files to move:   {stats['scanned']}")
       else:
          print(f"Files moved:     {stats['moved']}")

       print(f"Collisions:      {stats['collisions']}")
       print(f"Errors:          {stats['errors']}")

       print("\nCategories:")

       for category, count in stats["categories"].items():
          print(f"  {category}: {count}")

       print("─" * 30)
    except PermissionError:
          print(f"Error: permission denied while accessing {folder}")
    except OSError as error:
         print(f"Error: filesystem operation failed: {error}")


if __name__ == "__main__":
    main()