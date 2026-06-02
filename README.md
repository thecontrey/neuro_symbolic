## Contents

- `schemas/` — JSON schemas for anonymized scenarios, extractor output, and proof graphs.
- `prompts/` — prompt templates for schema-constrained extraction and end-to-end LLM+RAG baseline.
- `data_anonymized/controlled_benchmark/controlled_benchmark_600.jsonl` — 600 anonymized scenario-level records.
- `data_anonymized/llm_to_logic/llm_to_logic_240.jsonl` — 240 LLM-to-logic scenario records with extraction metadata.
- `data_anonymized/adaptation_subset/public_contract_russian_law_200.jsonl` — 200 adaptation subset records.
- `data_anonymized/cognitive_verification/cognitive_verification_item_level_216.csv` — anonymized cognitive verification rows.
- `outputs/predictions/` — scenario-level prediction files.
- `outputs/aggregate_metrics/` — aggregate tables reported in the paper.
- `proof_graphs/` — proof graph in JSON and DOT.
- `baselines/` — minimal baseline and symbolic reasoner scripts.
- `evaluation/` — metric, bootstrap, and validation utilities.
- `figures/` — architecture figure sources.

