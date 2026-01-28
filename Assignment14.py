# Database Systems (CSCI 331)
# Winter 2026
# Assignment 14 - Indexing and Query Optimization
# Zohaib Cheema

import DBUtil


def main():
    db = "meta"
    user = "Zohaib"
    assignment = "14"
    file_name = f"Assignment{assignment}.sql"

    # Read and run queries from SQL file
    DBUtil.read_and_run_queries(file_name, db, user, assignment)


if __name__ == "__main__":
    main()
