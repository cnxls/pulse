# Pulse

[![CI](https://github.com/cnxls/pulse/actions/workflows/ci.yml/badge.svg)](https://github.com/cnxls/pulse/actions/workflows/ci.yml)

Subscription product intelligence platform. Ingests app usage data, models churn
and lifetime value, forecasts key metrics, detects anomalies, and exposes an LLM
analyst copilot that answers questions in plain language and drafts retention
actions.

## Architecture

```
CSV sources ──> ingestion ──> Postgres ──> feature build ──> models (churn, LTV)
                                  │                              │
                                  │                              ├─> forecasting
                                  │                              └─> anomaly detection
                                  └────────────────────────────> LLM copilot (Q&A + retention drafts)
```

## Dataset

KKBox churn (WSDM Cup). Real subscription transactions, member records, and churn
labels. The `data/` directory is gitignored; download `members_v3.csv`,
`transactions_v2.csv`, and `train_v2.csv` from the competition page and place them
there.

## Setup

Requires Python 3.13, Poetry, and Docker.

```
poetry install
cp .env.example .env
docker compose up -d
```

This gives you the dependencies installed, a local `.env`, and Postgres running
on port 2345.

Run the ingestion load:

```
poetry run python src/ingestion/load_data.py
```

## Development

```
poetry run ruff check .
poetry run pytest
```

CI runs both on every push and pull request.

## Roadmap

- Ingestion and local Postgres schema
- Feature build from transactions and member data
- Churn model with real labels
- Lifetime value model
- Metric forecasting
- Anomaly detection on key metrics
- LLM analyst copilot over the modeled data

## What this demonstrates

- End-to-end data pipeline from raw files to a queryable database
- Supervised modeling on a real, labeled subscription dataset
- Time series forecasting and anomaly detection
- Retrieval and tool use for an LLM interface over structured data
- Reproducible setup, containerized dependencies, and CI from the first commit
