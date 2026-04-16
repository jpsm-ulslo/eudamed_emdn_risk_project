import pandas as pd

RISK_MAP = {
    "I": "Class I",
    "IIA": "Class IIa",
    "IIB": "Class IIb",
    "III": "Class III"
}

def normalize_risk_class():
    df = pd.read_csv("data/processed/basic_udi_normalized.csv")
    df["risk_class_norm"] = df["RISK_CLASS"].map(RISK_MAP)

    df.to_csv("data/processed/basic_udi_with_risk.csv", index=False)
    print("✅ Classe de risco normalizada")

if __name__ == "__main__":
    normalize_risk_class()