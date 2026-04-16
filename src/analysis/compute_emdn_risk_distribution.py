import pandas as pd
from src.utils.logging import log

def compute_distribution():
    df = pd.read_csv("data/processed/basic_udi_normalized.csv")

    agg = (
        df.groupby(["EMDN_CODE", "RISK_CLASS"])
          .size()
          .unstack(fill_value=0)
    )

    pct = (agg.div(agg.sum(axis=1), axis=0) * 100).round(1)
    pct["n_devices"] = agg.sum(axis=1)

    pct.reset_index().to_csv(
        "data/analytics/emdn_risk_distribution.csv",
        index=False
    )

    log("EMDN risk distribution created")

if __name__ == "__main__":
    compute_distribution()