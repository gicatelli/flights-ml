from pathlib import Path
import gdown

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "airlines.csv": "1R7CXjnud_PceDr6xLITAB0ZJpJVRBbTM",
    "airports.csv": "1e1Gvpsk9urYA2tSDBuJ4YPZfELvj89yZ",
    "flights.csv": "1ceyRYUzkF22E_PvwKBF0s2oyhWZpRGGN",
}

for filename, file_id in FILES.items():
    output_path = RAW_DIR / filename

    if output_path.exists():
        print(f"{filename} já existe. Pulando download.")
        continue

    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Baixando {filename}...")
    gdown.download(url, str(output_path), quiet=False)

print("Download concluído.")