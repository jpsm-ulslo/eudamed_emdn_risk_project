import json
import pandas as pd
from src.utils.logging import log

def normalize_basic_udi():
    with open("data/raw/eudamed_test/udi_all_test.json", encoding="utf-8") as f:
        records = json.load(f)

    df = pd.DataFrame(records)

    df_basic = (
        df.query("LATEST_VERSION == True")
          .drop_duplicates(subset=["BASIC_UDI"])
    )

    df_basic.to_csv("data/processed/basic_udi_normalized.csv", index=False)
    log(f"Basic UDI normalized: {len(df_basic)}")

if __name__ == "__main__":
    normalize_basic_udi()
