import urllib.request
import json
import html
import time
from src.utils.logging import log

def fetch_all_pages(start_url: str, headers: dict, max_pages: int, delay: float):
    """
    Generic EUDAMED paginator.
    Follows nextLink / @odata.nextLink until exhaustion.
    """
    records = []
    url = start_url
    page = 0

    while url:
        page += 1
        log(f"Fetching page {page}")

        if page > max_pages:
            raise RuntimeError("Safety stop: max_pages exceeded")

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode("utf-8"))

        batch = data.get("value", [])
        log(f"Records on page {page}: {len(batch)}")
        records.extend(batch)

        next_link = data.get("nextLink") or data.get("@odata.nextLink")
        url = html.unescape(next_link) if next_link else None

        time.sleep(delay)

    return records
