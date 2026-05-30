# Python Scripts

Python automation scripts built for real personal use on Windows. Covers file system management and process automation.

---

## Scripts

### `organize_downloads.py`
Automatically sorts the Downloads folder into categorized subfolders by file type.

**How it works:**
- Scans every file in `~/Downloads`
- Matches each file's extension against a defined category map
- Moves the file into the matching subfolder (creates it if it doesn't exist)
- Handles filename collisions by appending a counter — never overwrites existing files

**Categories handled:**

| Folder | Extensions |
|--------|------------|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.webp` |
| Videos | `.mp4` `.mov` `.mkv` `.avi` |
| PDFs | `.pdf` |
| Archives | `.zip` `.rar` `.7z` `.iso` |
| Documents | `.docx` `.txt` `.xlsx` `.csv` `.pptx` |
| Installers | `.exe` `.msi` `.msix` `.pkg` |
| Audio | `.mp3` `.wav` `.m4a` |

**Usage:**
```bash
python organize_downloads.py
```

---

### `pc_startup.py`
Launches a set of personal applications on Windows startup with a single script.

**How it works:**
- Resolves the current user's home directory dynamically using `Path.home()` — no hardcoded usernames
- Launches each app using `subprocess.Popen` with error handling per process
- Prints launch status for each application

**Usage:**
```bash
python pc_startup.py
```

> Update the `apps` list with your own application paths before running.

---

## Concepts Demonstrated

- File system operations with `pathlib.Path`
- File moving and directory creation with `shutil`
- Collision-safe file handling
- Process automation with `subprocess.Popen`
- Dynamic path resolution (no hardcoded usernames)
- Exception handling per subprocess

## Skills Demonstrated

`Python` `Automation` `File I/O` `pathlib` `shutil` `subprocess` `Windows` `Scripting`

---

### `subnet_calc.py`
A subnet calculator written in Python. You can input any IP address (in CIDR notation) and get your key network details.

## Output
- Network Address
- Broadcast Address
- Subnet mask
- Usable Host Ranges
- A Number of usable hosts

## Usage

```bash
python subnet_calc.py
```

Then enter an IP in CIDR format:

Type 'quit' to exit.

## Requirements
- Python 3.x
- No external libraries -- I used Python's built-in `ipaddress` module

## Background
Built as a practical networking utility while studying for CompTIA Network+ and 
taking network courses at CUNY New York City College of Technology. 
Useful for quickly referencing subnet details without manual calculation.

## Status
Work in progress -- core functionality is stable.

## Environment

- Python 3.10+
- Windows 10/11
