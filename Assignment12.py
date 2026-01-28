# Database Systems (CSCI 331)
# Winter 2026
# Assignment 12 - Database Table and Record Storage
# Zohaib Cheema

import DBUtil
import OutputUtil as ou


def main():
    db = "university"
    user = "Zohaib"
    assignment = "12"
    file_name = f"Assignment{assignment}.sql"

    # Read and run queries from SQL file (regular format)
    DBUtil.read_and_run_queries(file_name, db, user, assignment)

    # Get list of university database tables
    udb_tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes",
                  "teaches", "time_slot"]

    # Create queries for each table with fixed format
    queries_f = []
    for table in udb_tables:
        sql = f"SELECT * FROM {table}"
        desc = f"Retrieve rows from {table} with fixed-length format"
        queries_f.append([sql, desc])

    # Run queries with fixed format
    html_tables_f = DBUtil.run_queries(queries_f, user, db, assignment, frmt="F")

    # Write fixed format HTML file
    output_file_f = f"Assignment{assignment}-fixed.html"
    title_f = f"Assignment {assignment} - Fixed-Length Format"
    ou.write_html_file_new(output_file_f, title_f, None, html_tables_f, True, None, True)

    # Create queries for each table with variable format
    queries_v = []
    for table in udb_tables:
        sql = f"SELECT * FROM {table}"
        desc = f"Retrieve rows from {table} with variable-length format"
        queries_v.append([sql, desc])

    # Run queries with variable format
    html_tables_v = DBUtil.run_queries(queries_v, user, db, assignment, frmt="V")

    # Write variable format HTML file
    output_file_v = f"Assignment{assignment}-variable.html"
    title_v = f"Assignment {assignment} - Variable-Length Format"
    ou.write_html_file_new(output_file_v, title_v, None, html_tables_v, True, None, True)


if __name__ == "__main__":
    main()
