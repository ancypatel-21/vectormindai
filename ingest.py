from pathlib import Path

def load_documents(folder="documents"):
    docs = []
    folder_path = Path(folder)

    for file_path in folder_path.glob("*.txt"):
        text = file_path.read_text().strip()
        if text:
            docs.append({
                "source": file_path.name,
                "text": text
            })

    return docs