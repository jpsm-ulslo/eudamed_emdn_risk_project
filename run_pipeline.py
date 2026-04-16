from src.ingest.download_emdn_v2 import download_emdn_v2
from src.ingest.download_udi import download_udi
from src.transform.normalize_basic_udi import normalize_basic_udi
from src.analysis.compute_emdn_risk_distribution import compute_distribution
from src.utils.logging import log

def run():
    log("Pipeline started")

    download_emdn_v2()
    download_udi()
    normalize_basic_udi()
    compute_distribution()

    log("Pipeline finished successfully")

if __name__ == "__main__":
    run()