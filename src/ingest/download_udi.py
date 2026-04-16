from pathlib import Path
import yaml
import json
from src.utils.pagination import fetch_all_pages
from src.utils.logging import log

def download_udi():
    with open("config/api_endpoints.yaml") as f:
        endpoints = yaml.safe_load(f)

    with open("config/settings.yaml") as f:
        settings = yaml.safe_load(f)

    env = endpoints["environment"]
    cfg = endpoints["eudamed"][env]

    base_url = cfg["base_url"]
    path = cfg["udi"]["path"]
    api_version = cfg["api_version"]

    start_url = f"{base_url}{path}?format=json&api-version={api_version}"
    headers = {"Accept": "application/json"}

    records = fetch_all_pages(
        start_url=start_url,
        headers=headers,
        max_pages=settings["safety"]["max_pages"],
        delay=settings["safety"]["page_delay_seconds"],
    )

    output_path = Path("data/raw/eudamed_test/udi_all_test.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f)

    log(f"Total UDI records saved: {len(records)}")

if __name__ == "__main__":
    download_udi()
