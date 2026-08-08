FILE_TYPES = {

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".tiff": "Images",

    # Audio
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".aac": "Music",
    ".ogg": "Music",
    ".m4a": "Music",

    # Video
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".wmv": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",

    # Programming / Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".jsx": "Code",
    ".tsx": "Code",
    ".c": "Code",
    ".h": "Code",
    ".cpp": "Code",
    ".hpp": "Code",
    ".java": "Code",
    ".rs": "Code",
    ".go": "Code",
    ".rb": "Code",
    ".php": "Code",
    ".swift": "Code",

    # Web
    ".html": "Web",
    ".htm": "Web",
    ".css": "Web",

    # Data / Configuration
    ".json": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".toml": "Data",
    ".sql": "Data",

    # Disk / System images
    ".iso": "Disk Images",
    ".img": "Disk Images",
}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}

# Application settings

UNKNOWN_FOLDER = "Other"

LOG_FILE = "file_sorter.log"

COLLISION_FORMAT = "{stem} ({counter}){suffix}"
