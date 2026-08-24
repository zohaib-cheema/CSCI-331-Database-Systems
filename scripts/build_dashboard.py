#!/usr/bin/env python3
"""Validate Assignment 14 EXPLAIN captures and build dashboard-ready JSON."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_STATES = {"Before index", "After index"}
REQUIRED_COLUMNS = {"table", "type", "key", "rows"}


def estimated_rows(plan: dict) -> int:
    rows_index = plan["columns"].index("rows")
    return sum(int(row[rows_index] or 0) for row in plan["rows"])


def query_access(plan: dict) -> tuple[str, str]:
    columns = plan["columns"]
    table_index = columns.index("table")
    type_index = columns.index("type")
    key_index = columns.index("key")
    query_rows = [row for row in plan["rows"] if row[table_index] == "query"]
    if not query_rows:
        raise ValueError(f'{plan["state"]} / {plan["label"]} has no query-table row')

    access_counts = Counter(str(row[type_index]) for row in query_rows)
    access = ", ".join(
        f"{name} ×{count}" if count > 1 else name
        for name, count in access_counts.items()
    )
    keys = sorted({str(row[key_index]) for row in query_rows if row[key_index]})
    return access, ", ".join(keys) if keys else "—"


def build(source: Path) -> dict:
    artifact = json.loads(source.read_text(encoding="utf-8"))
    plans = artifact.get("plans")
    if not isinstance(plans, list) or len(plans) != 10:
        raise ValueError("Expected exactly 10 captured plans (five before and five after)")

    states = {plan.get("state") for plan in plans}
    if states != REQUIRED_STATES:
        raise ValueError(f"Expected states {sorted(REQUIRED_STATES)}, found {sorted(states)}")

    pairs: dict[str, dict[str, dict]] = {}
    for plan in plans:
        missing = REQUIRED_COLUMNS.difference(plan.get("columns", []))
        if missing:
            raise ValueError(f'{plan.get("label", "Plan")} is missing columns: {sorted(missing)}')
        if not plan.get("rows"):
            raise ValueError(f'{plan["state"]} / {plan["label"]} has no captured rows')
        pairs.setdefault(plan["label"], {})[plan["state"]] = plan

    if len(pairs) != 5 or any(set(pair) != REQUIRED_STATES for pair in pairs.values()):
        raise ValueError("Every query must have one before and one after plan")

    query_metrics = []
    for label, pair in pairs.items():
        before = pair["Before index"]
        after = pair["After index"]
        before_access, before_key = query_access(before)
        after_access, after_key = query_access(after)
        query_metrics.append(
            {
                "label": label.replace("Query ", "Q").replace(": ", " · "),
                "fullLabel": label,
                "beforeRows": estimated_rows(before),
                "afterRows": estimated_rows(after),
                "beforeAccess": before_access,
                "afterAccess": after_access,
                "beforeKey": before_key,
                "afterKey": after_key,
            }
        )

    filtered = query_metrics[1:]
    indexed_before = sum(item["beforeKey"] != "—" for item in filtered)
    indexed_after = sum(item["afterKey"] == "idx_query_assn" for item in filtered)
    union = query_metrics[-1]
    reduction = round((1 - union["afterRows"] / union["beforeRows"]) * 100, 1)

    return {
        "source": source.name,
        "methodology": "MySQL EXPLAIN row estimates from the captured before/after plans; not measured physical reads.",
        "summary": {
            "planCount": len(plans),
            "planRowCount": sum(len(plan["rows"]) for plan in plans),
            "filteredQueryCount": len(filtered),
            "indexedBefore": indexed_before,
            "indexedAfter": indexed_after,
            "unionBeforeRows": union["beforeRows"],
            "unionAfterRows": union["afterRows"],
            "unionReductionPercent": reduction,
        },
        "queries": query_metrics,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("Assignment14_explain.json"))
    parser.add_argument("--output", type=Path, default=Path("dashboard-data.json"))
    args = parser.parse_args()
    dashboard = build(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(dashboard, indent=2) + "\n", encoding="utf-8")
    print(
        f'Validated {dashboard["summary"]["planCount"]} plans and wrote {args.output}'
    )


if __name__ == "__main__":
    main()
