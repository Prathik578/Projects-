# FilePilot

FilePilot is a lightweight, configurable command-line file organizer written in Python.

It automatically scans a directory, classifies files by their extensions, and moves them into organized category folders while protecting existing files from accidental overwrites.

The project focuses on safe filesystem operations, predictable behavior, configurability, recursive organization, dry-run support, logging, statistics, and automated testing.

---

## Table of Contents

- [Features](#features)
  - [1. Automatic File Organization](#1-automatic-file-organization)
  - [2. Extension-Based Classification](#2-extension-based-classification)
  - [3. Multiple File Categories](#3-multiple-file-categories)
  - [4. Recursive Directory Scanning](#4-recursive-directory-scanning)
  - [5. Destination Directory Protection](#5-destination-directory-protection)
  - [6. Excluded Directories](#6-excluded-directories)
  - [7. Collision Protection](#7-collision-protection)
  - [8. Dry-Run Mode](#8-dry-run-mode)
  - [9. Command-Line Interface](#9-command-line-interface)
  - [10. Input Validation](#10-input-validation)
  - [11. Permission Error Handling](#11-permission-error-handling)
  - [12. File Operation Logging](#12-file-operation-logging)
  - [13. Sorting Statistics](#13-sorting-statistics)
  - [14. Configurable Unknown File Handling](#14-configurable-unknown-file-handling)
  - [15. Configurable Collision Naming](#15-configurable-collision-naming)
  - [16. Configurable Exclusions](#16-configurable-exclusions)
  - [17. Standard Library Based Core](#17-standard-library-based-core)
  - [18. Automated Testing](#18-automated-testing)
  - [19. Collision Testing](#19-collision-testing)
  - [20. Dry-Run Testing](#20-dry-run-testing)
  - [21. Recursive Sorting Testing](#21-recursive-sorting-testing)
  - [22. Exclusion Testing](#22-exclusion-testing)
- [Project Architecture](#project-architecture)
- [Configuration Overview](#configuration-overview)
- [Safety Philosophy](#safety-philosophy)
- [Design Goals](#design-goals)
- [Current Capabilities](#current-capabilities)
- [Project Status](#project-status)
- [License](#license)
- [Author](#author)

---

## Features

### 1. Automatic File Organization

FilePilot automatically identifies files based on their extensions and moves them into appropriate category directories.

**Example:**

| Source File | Destination |
|-------------|-------------|
| `homework.pdf` | `Documents/` |
| `report.docx` | `Documents/` |
| `photo.jpg` | `Images/` |
| `song.mp3` | `Music/` |
| `movie.mp4` | `Videos/` |
| `project.py` | `Code/` |
| `archive.zip` | `Archives/` |

Files are organized without requiring the user to manually create destination folders.

FilePilot automatically creates the required category directory when necessary.

---

### 2. Extension-Based Classification

File classification is controlled through `config.py`.

Each extension can be mapped to a category.

**Example:**

```python
FILE_TYPES = {
    ".pdf": "Documents",
    ".jpg": "Images",
    ".mp3": "Music",
    ".py": "Code",
}
```

File extensions are normalized to lowercase before classification.

Therefore:

```
PHOTO.JPG
photo.jpg
Photo.Jpg
```

are all classified as image files.

---

### 3. Multiple File Categories

FilePilot currently supports a broad range of common file types.

#### Documents

| Extensions | Destination |
|------------|-------------|
| `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt` | `Documents/` |

#### Spreadsheets

| Extensions | Destination |
|------------|-------------|
| `.xls`, `.xlsx`, `.csv`, `.ods` | `Spreadsheets/` |

#### Presentations

| Extensions | Destination |
|------------|-------------|
| `.ppt`, `.pptx`, `.odp` | `Presentations/` |

#### Images

| Extensions | Destination |
|------------|-------------|
| `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.bmp`, `.svg`, `.tiff` | `Images/` |

#### Music

| Extensions | Destination |
|------------|-------------|
| `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a` | `Music/` |

#### Videos

| Extensions | Destination |
|------------|-------------|
| `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.wmv` | `Videos/` |

#### Archives

| Extensions | Destination |
|------------|-------------|
| `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz` | `Archives/` |

#### Programming / Source Code

| Extensions | Destination |
|------------|-------------|
| `.py`, `.js`, `.ts`, `.jsx`, `.tsx`, `.c`, `.h`, `.cpp`, `.hpp`, `.java`, `.rs`, `.go`, `.rb`, `.php`, `.swift` | `Code/` |

#### Web Files

| Extensions | Destination |
|------------|-------------|
| `.html`, `.htm`, `.css` | `Web/` |

#### Data / Configuration

| Extensions | Destination |
|------------|-------------|
| `.json`, `.xml`, `.yaml`, `.yml`, `.toml`, `.sql` | `Data/` |

#### Disk Images

| Extensions | Destination |
|------------|-------------|
| `.iso`, `.img` | `Disk Images/` |

#### Unknown Files

Files whose extensions are not recognized are placed into:

```
Other/
```

The default unknown-file category is configurable.

---

### 4. Recursive Directory Scanning

FilePilot can scan directories recursively.

**For example:**

```
project/
├── homework.pdf
├── school/
│   └── assignment.pdf
└── photos/
    └── image.jpg
```

FilePilot can discover all of these files:

```
project/homework.pdf
project/school/assignment.pdf
project/photos/image.jpg
```

and organize them into:

```
project/
├── Documents/
│   ├── homework.pdf
│   └── assignment.pdf
│
└── Images/
    └── image.jpg
```

This allows FilePilot to organize files even when they are buried inside nested directories.

---

### 5. Destination Directory Protection

Recursive scanning introduces an important problem:

FilePilot creates directories such as:

```
Documents/
Images/
Music/
Videos/
```

If those directories were scanned again, FilePilot could attempt to process its own output.

FilePilot prevents this by recognizing its configured output directories and excluding them from recursive traversal.

This prevents unnecessary reprocessing and recursive behavior.

---

### 6. Excluded Directories

FilePilot supports directories that should never be scanned.

The default excluded directories include:

| Directory | Purpose |
|-----------|---------|
| `.git` | Git version control |
| `.venv` | Python virtual environment |
| `__pycache__` | Python bytecode cache |
| `node_modules` | Node.js dependencies |

These directories are controlled through:

```python
EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}
```

This is particularly useful when organizing development projects.

**For example:**

```
project/
├── .git/
├── .venv/
├── __pycache__/
├── node_modules/
└── source files
```

FilePilot will leave the excluded directories untouched.

---

### 7. Collision Protection

FilePilot never intentionally overwrites an existing destination file.

Suppose:

```
Documents/homework.pdf
```

already exists.

If another:

```
homework.pdf
```

is being moved into the same directory, FilePilot generates a unique filename.

The result becomes:

```
Documents/homework.pdf
Documents/homework (1).pdf
```

If another collision occurs:

```
Documents/homework (2).pdf
```

and so on.

The collision naming format is configurable:

```python
COLLISION_FORMAT = "{stem} ({counter}){suffix}"
```

FilePilot checks for available filenames before moving the file.

This prevents existing files from being silently destroyed.

---

### 8. Dry-Run Mode

FilePilot supports a dry-run mode that previews operations without moving files.

**Example:**

```
Would move: dry_run_test/mystery.xyz → dry_run_test/Other/mystery.xyz
Would move: dry_run_test/homework.pdf → dry_run_test/Documents/homework.pdf
Would move: dry_run_test/photo.jpg → dry_run_test/Images/photo.jpg
```

Dry-run mode is useful when the user wants to inspect the planned changes before allowing FilePilot to modify the filesystem.

No files are moved during a dry run.

---

### 9. Command-Line Interface

FilePilot can be operated from the command line.

**Example:**

```bash
python3 main.py /path/to/folder
```

It also supports dry-run execution:

```bash
python3 main.py /path/to/folder --dry-run
```

The application validates the supplied path before attempting to process it.

---

### 10. Input Validation

FilePilot detects invalid input paths.

| Scenario | Error Message |
|----------|---------------|
| Folder does not exist | `Error: folder does not exist: doesnot_exist` |
| Path is a file, not a directory | `Error: not a directory: test_file.txt` |

This prevents the application from attempting to perform directory operations on invalid paths.

---

### 11. Permission Error Handling

FilePilot also handles directories that cannot be accessed because of insufficient permissions.

**For example:**

```
Error: permission denied while accessing /root
```

This provides a clear error message instead of exposing an unhandled Python traceback to the user.

---

### 12. File Operation Logging

Successful move operations are recorded in the configured log file.

| Setting | Value |
|---------|-------|
| Default log file | `file_sorter.log` |

**Example:**

```
[2026-08-08 18:30:21] MOVED: homework.pdf → Documents/homework.pdf
```

The log records:

| Field | Description |
|-------|-------------|
| Timestamp | Date and time of the operation |
| Action | Type of operation performed |
| Source path | Original file location |
| Destination path | New file location |

This provides a basic audit trail of file operations.

---

### 13. Sorting Statistics

FilePilot tracks statistics during every sorting operation.

The statistics include:

| Statistic | Description |
|-----------|-------------|
| Files scanned | Total number of files discovered |
| Files moved | Number of files successfully moved |
| Collisions | Number of filename collisions resolved |
| Errors | Number of errors encountered |
| Files per category | Breakdown by destination category |

**Example:**

```
──────────────────────────────
FilePilot Summary
──────────────────────────────
Files scanned:   4
Files to move:   4
Collisions:      0
Errors:          0

Categories:
  Other:     1
  Documents: 2
  Images:    1
──────────────────────────────
```

This gives the user a clear summary of the operation.

---

### 14. Configurable Unknown File Handling

Unknown file types are not discarded.

If an extension does not exist in `FILE_TYPES`, FilePilot places the file into the configured unknown category.

| Setting | Default |
|---------|---------|
| `UNKNOWN_FOLDER` | `"Other"` |

**Example:**

```
mystery.xyz → Other/mystery.xyz
```

This ensures that unrecognized files are still organized instead of being ignored.

---

### 15. Configurable Collision Naming

The collision naming system is configurable.

| Setting | Default |
|---------|---------|
| `COLLISION_FORMAT` | `"{stem} ({counter}){suffix}"` |

**For example:**

```
report.pdf
report (1).pdf
report (2).pdf
```

The format can be changed to suit different naming preferences.

---

### 16. Configurable Exclusions

Users can modify the directories excluded from recursive scanning.

**Example:**

```python
EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "custom_directory",
}
```

This allows FilePilot to adapt to different workflows.

---

### 17. Standard Library Based Core

FilePilot's core functionality is implemented using Python's standard library.

| Module | Purpose |
|--------|---------|
| `pathlib` | Object-oriented filesystem paths |
| `os` | Operating system interfaces |
| `shutil` | High-level file operations |
| `datetime` | Date and time handling |

The project does not require a database, external API, or heavyweight framework.

This keeps the application lightweight and portable.

---

### 18. Automated Testing

FilePilot includes an automated test suite using `pytest`.

| Metric | Value |
|--------|-------|
| Total tests | 6 |
| Tests passing | 6 |

The test suite covers:

| Test | Description |
|------|-------------|
| Normal file sorting | Basic extension-based organization |
| Unknown file handling | Files with unrecognized extensions |
| Collision handling | Filename conflict resolution |
| Dry-run behavior | Preview mode without filesystem changes |
| Recursive sorting | Nested directory traversal |
| Excluded directories | Skipping protected directories |

**Example test result:**

```
============================================ test session starts =============================================

platform linux -- Python 3.12.3

collected 6 items

tests/test_sorter.py ......                                                                            [100%]

============================================= 6 passed in 0.08s =============================================
```

---

### 19. Collision Testing

The collision system has dedicated automated coverage.

The test creates an existing:

```
Documents/homework.pdf
```

and then attempts to sort another:

```
homework.pdf
```

The expected result is:

```
Documents/homework.pdf
Documents/homework (1).pdf
```

The original file must remain untouched.

This verifies that collision handling protects existing data.

---

### 20. Dry-Run Testing

Dry-run behavior is tested to ensure that previewing an operation does not actually move files.

This is important because dry-run mode is intended to be a safety mechanism.

---

### 21. Recursive Sorting Testing

Recursive sorting is tested using nested directories.

**Example:**

```
recursive_sort_test/
├── root.txt
├── school/
│   └── homework.pdf
└── photos/
    └── image.jpg
```

FilePilot correctly identifies files at different directory depths and organizes them into the appropriate output categories.

---

### 22. Exclusion Testing

Excluded-directory behavior is also tested.

A file inside an excluded directory must remain untouched.

**For example:**

```
.git/
    important.pdf
```

must not result in:

```
Documents/important.pdf
```

The original file remains in the excluded directory.

---

## Project Architecture

The project is separated into several components.

```
File-Sorter/
│
├── main.py
│
├── sorter.py
│
├── config.py
│
├── utils.py
│
├── tests/
│   └── test_sorter.py
│
├── pytest.ini
│
├── pyproject.toml
│
├── README.md
│
├── LICENSE
│
└── .gitignore
```

| File | Purpose |
|------|---------|
| `main.py` | Handles the command-line interface and application entry point |
| `sorter.py` | Contains the core filesystem sorting logic |
| `config.py` | Contains file categories, excluded directories, unknown-file behavior, logging configuration, and collision naming configuration |
| `utils.py` | Contains supporting utility functionality |
| `tests/` | Contains automated tests for the core sorting behavior |
| `pytest.ini` | pytest configuration |
| `pyproject.toml` | Project packaging and build configuration |
| `README.md` | Project documentation |
| `LICENSE` | MIT License |
| `.gitignore` | Git ignore rules |

---

## Configuration Overview

The main configuration values include:

```python
FILE_TYPES = {...}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}

UNKNOWN_FOLDER = "Other"

LOG_FILE = "file_sorter.log"

COLLISION_FORMAT = "{stem} ({counter}){suffix}"
```

This keeps application behavior separate from the sorting implementation.

---

## Safety Philosophy

FilePilot is designed around a simple principle:

> **Organizing files should not mean risking them.**

Therefore, the application uses several safeguards:

| Safeguard | Description |
|-----------|-------------|
| Existing file preservation | Destination files are never overwritten |
| Collision handling | Unique filenames are generated automatically |
| Dry-run mode | Preview operations before committing changes |
| Excluded directories | Protected directories are never scanned |
| Destination protection | Generated output directories are not reprocessed |
| Input validation | Invalid paths are rejected immediately |
| Permission handling | Access failures are reported clearly |
| Operation logging | All moves are recorded for audit |
| Automated testing | Critical behavior is verified by tests |

---

## Design Goals

FilePilot was designed around five core goals.

| Goal | Description |
|------|-------------|
| **Safety** | Protect existing files and avoid destructive operations |
| **Predictability** | Make file movements understandable before they happen |
| **Configurability** | Allow users to define their own categories and behavior |
| **Simplicity** | Keep the implementation lightweight and understandable |
| **Testability** | Use automated tests to verify filesystem behavior |

---

## Current Capabilities

FilePilot currently provides:

- Extension-based file classification
- Multiple file categories
- Recursive scanning
- Automatic category directory creation
- Destination directory protection
- Configurable excluded directories
- Unknown file handling
- Collision detection
- Automatic unique filenames
- Dry-run mode
- CLI path validation
- Permission error handling
- File operation logging
- Sorting statistics
- Configurable file mappings
- Configurable collision naming
- Automated pytest coverage

---

## Project Status

FilePilot has completed its core v1 feature set.

| Metric | Value |
|--------|-------|
| Total tests | 6 |
| Tests passing | 6 |

The project is currently in the final release and packaging stage.

---

## License

FilePilot is released under the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

---

## Author

**Prathik**

FilePilot is a practical software engineering project focused on filesystem automation, Python programming, command-line application design, defensive programming, configuration management, and automated testing.
