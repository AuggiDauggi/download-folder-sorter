from pathlib import Path
from PyPDF2 import PdfReader


def read_pdf(path):

    text = ""

    try:
        reader = PdfReader(path)

        for page in reader.pages:
            text += page.extract_text() or ""

    except Exception as e:
        print(f"PDF error: {e}")

    return text


def extract_content(file_path):

    suffix = Path(file_path).suffix.lower()

    if suffix in [
        ".txt",
        ".md",
        ".py",
        ".js",
        ".html",
        ".css",
        ".json",
        ".csv"
    ]:

        try:
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                return f.read()

        except Exception:
            return Path(file_path).name

    elif suffix == ".pdf":

        return read_pdf(file_path)

    elif suffix in [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp"
    ]:

        return f"Image file named {Path(file_path).name}"

    elif suffix in [
        ".zip",
        ".rar",
        ".7z"
    ]:

        return f"Archive file named {Path(file_path).name}"

    return Path(file_path).name
