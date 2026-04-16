import pandas as pd
from src.utils.logging import log

def compute_distribution():
    # Distribuição empírica
    df = pd.read_csv("data/processed/basic_udi_with_risk.csv")

    dist = (
        df.groupby(["EMDN_CODE", "risk_class_norm"])
          .size()
          .unstack(fill_value=0)
    )

    dist_pct = (dist.div(dist.sum(axis=1), axis=0) * 100).round(1)
    dist_pct["n_devices"] = dist.sum(axis=1)
    dist_pct = dist_pct.reset_index()

    # 🔗 Carregar EMDN v2 para texto legível
    emdn = pd.read_csv("data/processed/emdn_v2_normalized.csv")

    # Selecionar apenas colunas relevantes
    emdn = emdn[[
        "EMDN_CODE",
        "EMDN_TERM",
        "EMDN_DESCRIPTION"
    ]].drop_duplicates()

    # 🔗 Join final
    result = dist_pct.merge(
        emdn,
        on="EMDN_CODE",
        how="left"
    )

    # Reordenar colunas para leitura humana
    cols = (
        ["EMDN_CODE", "EMDN_TERM", "EMDN_DESCRIPTION"] +
        [c for c in result.columns if c.startswith("Class")] +
        ["n_devices"]
    )

    result = result[cols]

    result.to_csv(
        "data/analytics/emdn_risk_distribution.csv",
        index=False
    )

    log("EMDN × risk distribution (with descriptions) created")

if __name__ == "__main__":
    compute_distribution()
