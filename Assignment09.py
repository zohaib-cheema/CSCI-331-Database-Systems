# Database Systems (CSCI 331)
# Winter 2026
# Assignment 09 - Database Design Normalization
# Zohaib Cheema

import DBUtil

def main():
    db = "books"
    user = "Zohaib"
    assignment = "09"
    file_name = f"Assignment{assignment}.sql"
    DBUtil.read_and_run_queries(file_name, db, user, assignment)


if __name__ == "__main__":
    main()
