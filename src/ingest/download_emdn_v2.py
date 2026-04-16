from pathlib import Path
import urllib.request
import pandas as pd
import yaml

from src.utils.logging import log

def download_emdn_v2():
    with open("config/settings.yaml") as f:
        settings = yaml.safe_load(f)

    emdn_cfg = settings["emdn"]["source"]

    url = emdn_cfg["url"]
    local_path = Path(emdn_cfg["local_path"])

    local_path.parent.mkdir(parents=True, exist_ok=True)

    if not local_path.exists():
        log(f"Downloading EMDN v2 from {url}")
        urllib.request.urlretrieve(url, local_path)
        log("EMDN v2 download completed")
    else:
        log("EMDN v2 file already exists, skipping download")

    # ✅ Inspect sheet names
    xls = pd.ExcelFile(local_path)
    sheets = xls.sheet_names
    log(f"Available EMDN sheets: {sheets}")

    # ✅ Heuristic: choose first non-empty sheet
    selected_sheet = sheets[0]
    log(f"Using EMDN sheet: {selected_sheet}")

    df = pd.read_excel(local_path, sheet_name=selected_sheet)
    df["emdn_version"] = settings["emdn"]["version"]

    output = Path("data/processed/emdn_v2_normalized.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)

    log(f"EMDN v2 loaded and normalized ({len(df)} rows)")

if __name__ == "__main__":
    download_emdn_v2()