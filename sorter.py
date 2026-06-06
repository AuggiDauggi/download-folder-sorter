from pathlib import Path
import shutil

from extractor import extract_content
from classifier import classify

DOWNLOADS = Path("downloads") #Change this to downloads folder you want to use
SORTED = Path("sorted")

DOWNLOADS.mkdir(exist_ok=True)
SORTED.mkdir(exist_ok=True)

for file in DOWNLOADS.iterdir():

    if not file.is_file():
        continue

    print("\n----------------------------")
    print(f"Processing: {file.name}")

    suffix = file.suffix.lower()

    try:

        # Images
        if suffix in [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp"
        ]:

            folder = "Images"
            reason = f"Image file ({suffix})"

        # Code
        elif suffix in [
            ".py",
            ".js",
            ".html",
            ".css",
            ".json"
        ]:

            folder = "Programming"
            reason = f"Code file ({suffix})"

        # Archives
        elif suffix in [
            ".zip",
            ".rar",
            ".7z"
        ]:

            folder = "Archives"
            reason = f"Archive file ({suffix})"

        # AI decides
        else:

            content = extract_content(file)

            existing_folders = [
                folder.name
                for folder in SORTED.iterdir()
                if folder.is_dir()
            ]

            result = classify(
                content,
                existing_folders
            )

            folder = result["folder"]
            reason = result["reason"]

        print("\nAI Decision")
        print(f"Folder: {folder}")
        print(f"Reason: {reason}")

        with open("sort_log.txt", "a") as log:

            log.write(
                f"{file.name} -> {folder}\n"
                f"Reason: {reason}\n\n"
            )

        destination = SORTED / folder

        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.move(
            str(file),
            str(destination / file.name)
        )

        print(f"Moved to {destination}")

    except Exception as e:

        print(f"Error processing {file.name}")
        print(e)
