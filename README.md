# EUDAMED – EMDN (v2) Risk Distribution Project

## Overview

This project builds an empirical, descriptive table that shows, for each
European Medical Device Nomenclature (EMDN v2) entry, the observed distribution
of MDR risk classes among devices registered in EUDAMED.

The analysis is explicitly:
- descriptive (not normative),
- reproducible,
- transparent about data and environment limitations,
- suitable for analytical and regulatory‑intelligence use.

---

## Important Disclaimer

THIS PROJECT PRODUCES DESCRIPTIVE ANALYTICS ONLY.

The resulting EMDN × risk‑class distributions are observed empirical patterns
and MUST NOT be used as regulatory classification under MDR/IVDR Annex VIII.

---

## Data Sources

- EUDAMED Public API
  - TEST environment (full pagination supported for UDI‑DI)
  - PROD environment (UDI‑DI hard‑capped; full enumeration not possible)
- European Medical Device Nomenclature (EMDN v2)
  - Official taxonomy published by the European Commission

---

## High‑Level Pipeline

1. Download and normalize EMDN v2
2. Download all UDI‑DI records from EUDAMED (TEST)
3. Reduce records to Basic UDI level
4. Normalize risk classes
5. Aggregate devices by EMDN v2
6. Compute percentage distribution per risk class

---

## Project Structure

```text
eudamed_emdn_risk_project/
├── README.md
├── requirements.txt
├── run_pipeline.py
│
├── config/
│   ├── api_endpoints.yaml
│   └── settings.yaml
│
├── data/
│   ├── raw/
│   │   ├── emdn_v2/
│   │   │   └── emdn_v2.xlsx
│   │   └── eudamed_test/
│   │       └── udi_all_test.json
│   │
│   ├── processed/
│   │   ├── emdn_v2_normalized.csv
│   │   ├── basic_udi_normalized.csv
│   │   └── basic_udi_with_risk.csv
│   │
│   └── analytics/
│       └── emdn_risk_distribution.csv
│
├── src/
│   ├── __init__.py
│   │
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── download_emdn_v2.py
│   │   └── download_udi.py
│   │
│   ├── transform/
│   │   ├── __init__.py
│   │   ├── normalize_basic_udi.py
│   │   └── normalize_risk_class.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── compute_emdn_risk_distribution.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── pagination.py
│       └── logging.py
``
---

## Configuration

config/api_endpoints.yaml defines:
- Active environment (TEST or PROD)
- Base URLs
- API versions
- Endpoint paths

config/settings.yaml defines:
- EMDN version (v2)
- Aggregation level (Basic UDI)
- Safety limits (maximum pages, pagination delay)
- Minimum sample thresholds per EMDN

No script hard‑codes API URLs.

---

## Environment Notes

TEST:
- /eudamed/udi fully paginates using nextLink
- Complete UDI‑DI universe can be extracted

PROD:
- /eudamed/udi is hard‑capped
- Full enumeration is NOT possible

This project is intended to run in TEST.

---

## Running the Pipeline

From the project root directory:

python run_pipeline.py

The pipeline:
- logs progress with timezone‑aware UTC timestamps,
- follows EUDAMED pagination correctly,
- writes intermediate and final datasets to the data directory.

---

## Output

data/analytics/emdn_risk_distribution.csv

Example structure:

EMDN_CODE,Class I,Class IIa,Class IIb,Class III,n_devices
R07,2.1,18.3,54.2,25.4,412

Percentages represent observed distributions, NOT regulatory assignments.

---

## Design Principles

- Config‑driven architecture
- Single shared pagination utility
- Timezone‑aware logging
- Basic UDI as aggregation unit
- Explicit non‑normative framing
- Environment awareness (TEST vs PROD)

---

## Intended Use

This project is intended for:
- analytical research,
- regulatory intelligence,
- technology‑domain and portfolio analysis.

It is NOT a substitute for regulatory classification or conformity assessment.
