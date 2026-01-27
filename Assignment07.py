# Database Systems (CSCI 331)
# Winter 2026
# Assignment 07 - Complex Data Types
# Zohaib Cheema

import DBUtil
import OutputUtil as ou


def main():
    db = "university"
    user = "Zohaib"
    assignment = "07"
    file_name = f"Assignment{assignment}.sql"
    
    # Read and run queries from SQL file
    DBUtil.read_and_run_queries(file_name, db, user, assignment)
    
    # [4] Backup all tables from university database
    udb_tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes",
                  "teaches", "time_slot"]
    
    for table in udb_tables:
        DBUtil.backup_table(table, user, db, assignment)
    
    # [6] Restore data for all tables and create HTML output
    html_tables = []
    for table in udb_tables:
        html_tables += DBUtil.restore_data(table, db, assignment, user)
    
    # Write restoration HTML file
    output_file = f"Assignment{assignment}-restoration.html"
    title = "Restoration of all original University Database Tables"
    ou.write_html_file_new(output_file, title, None, html_tables, True, None, True)


if __name__ == "__main__":
    main()
