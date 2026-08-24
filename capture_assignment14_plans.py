"""Capture Assignment 14 EXPLAIN plans without writing to the query log."""

import argparse
import json
from pathlib import Path

import pymysql


QUERIES = [
    ("Query 1: COUNT(*)", "SELECT COUNT(*) FROM `query`"),
    (
        "Query 2: IN clause",
        "SELECT COUNT(*) FROM `query` WHERE query_assn IN "
        "('03','04','05','06','07','08','09','10','11','12','13','14')",
    ),
    (
        "Query 3: OR clause",
        "SELECT COUNT(*) FROM `query` WHERE "
        + " OR ".join(f"query_assn = '{value:02d}'" for value in range(3, 15)),
    ),
    (
        "Query 4: LIKE clause",
        "SELECT COUNT(*) FROM `query` WHERE "
        + " OR ".join(f"query_assn LIKE '{value:02d}'" for value in range(3, 15)),
    ),
    (
        "Query 5: UNION ALL",
        "SELECT SUM(cnt) AS total FROM ("
        + " UNION ALL ".join(
            f"SELECT COUNT(*) AS cnt FROM `query` WHERE query_assn = '{value:02d}'"
            for value in range(3, 15)
        )
        + ") AS subquery",
    ),
]


def capture(cursor, state):
    plans = []
    for label, sql in QUERIES:
        cursor.execute("EXPLAIN " + sql)
        columns = [column[0] for column in cursor.description]
        plans.append(
            {
                "state": state,
                "label": label,
                "sql": sql,
                "columns": columns,
                "rows": [list(row) for row in cursor.fetchall()],
            }
        )
    return plans


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password-file", required=True)
    parser.add_argument("--output", default="Assignment14_explain.json")
    args = parser.parse_args()

    password = Path(args.password_file).read_text(encoding="utf-8").strip()
    connection = pymysql.connect(
        host="localhost", user="root", password=password, database="meta"
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM information_schema.statistics "
                "WHERE table_schema='meta' AND table_name='query' "
                "AND index_name='idx_query_assn'"
            )
            index_existed = cursor.fetchone()[0] > 0

            if index_existed:
                cursor.execute("DROP INDEX idx_query_assn ON `query`")
            plans = capture(cursor, "Before index")

            cursor.execute("CREATE INDEX idx_query_assn ON `query` (query_assn)")
            plans.extend(capture(cursor, "After index"))

            if not index_existed:
                cursor.execute("DROP INDEX idx_query_assn ON `query`")

        connection.commit()
    finally:
        connection.close()

    Path(args.output).write_text(
        json.dumps({"plans": plans}, indent=2, default=str) + "\n", encoding="utf-8"
    )
    print(f"Captured {len(plans)} execution plans in {args.output}")


if __name__ == "__main__":
    main()
