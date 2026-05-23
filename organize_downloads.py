from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi"],
    "PDFs": [".pdf"],
    "Archives": [".zip", ".rar", ".7z", ".iso"],
    "Documents": [".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Installers": [".exe", ".msi", ".msix", ".pkg"],
    "Audio": [".mp3", ".wav", ".m4a"]
}

for file in downloads.iterdir():
    if file.is_file():
        for folder_name, extensions in folders.items():
            if file.suffix.lower() in extensions:
                target_folder = downloads / folder_name
                target_folder.mkdir(exist_ok=True)
                destination = target_folder / file.name

                # Prevent overwrite — append counter if file already exists
                counter = 1
                while destination.exists():
                    destination = target_folder / f"{file.stem}_{counter}{file.suffix}"
                    counter += 1

                shutil.move(str(file), str(destination))
                print(f"Moved: {file.name} -> {target_folder.name}/")
                break

print("Downloads folder organized.")
