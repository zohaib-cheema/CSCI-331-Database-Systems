# Database Systems (CSCI 331)
# Winter 2026
# Assignment 09 - Database Design and Authorization
# Zohaib Cheema

import DBUtil

def main():
    db = "university"
    user = "Zohaib"
    assignment = "10"
    file_name = f"Assignment{assignment}.sql"
    DBUtil.read_and_run_queries(file_name, db, user, assignment)


if __name__ == "__main__":
    main()