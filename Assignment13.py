# Database Systems (CSCI 331)
# Winter 2026
# Assignment 13 - Pivot Tables in SQL
# Zohaib Cheema

import DBUtil
import OutputUtil as ou


def make_pivot_table(assn, user, db, table, column_x, column_y, column_val):
    """
    Helper function to create a pivot table and write it to HTML file.
    """
    title, headers, types, alignments, data = DBUtil.pivot_table(assn, user, db, table, column_x, column_y, column_val)
    file_name = f"Assignment{assn}-{db}-{table}.html"
    ou.write_html_file(file_name, title, headers, types, alignments, data, True)


def main():
    user = "Zohaib"
    assignment = "13"
    file_name = f"Assignment{assignment}.sql"

    # Step 1: Create the sales database (connect to mysql first)
    create_db_queries = [
        ["DROP SCHEMA IF EXISTS sales", "Drop schema sales if it exists"],
        ["CREATE SCHEMA sales", "Create schema sales"],
    ]
    DBUtil.run_queries(create_db_queries, user, "mysql", assignment)
    
    # Step 2: Read queries and filter out DROP/CREATE SCHEMA (already done) and USE (not needed)
    all_queries = DBUtil.read_queries(file_name)
    filtered_queries = []
    for sql, desc in all_queries:
        sql_upper = sql.upper().strip()
        # Skip schema operations (already done) and USE (connecting directly to sales)
        if "DROP SCHEMA" in sql_upper or "CREATE SCHEMA" in sql_upper or "USE" in sql_upper:
            continue
        filtered_queries.append([sql, desc])
    
    # Step 3: Run filtered queries on sales database (includes DROP TABLE, CREATE TABLE, INSERT, SELECT)
    html_tables = DBUtil.run_queries(filtered_queries, user, "sales", assignment)
    
    # Step 4: Add analytics
    analytics_queries = DBUtil.add_analytics(assignment)
    analytics_tables = DBUtil.run_queries(analytics_queries, user, "sales", assignment)
    html_tables.extend(analytics_tables)
    
    # Step 5: Write HTML file
    output_file = f"Assignment{assignment}.html"
    title = f"Assignment{assignment}"
    ou.write_html_file_new(output_file, title, None, html_tables, True, None, True)
    
    # Step 6: Verify data was inserted
    verify_query = "SELECT COUNT(*) as row_count FROM sale"
    verify_desc = "Verify data was inserted into sale table"
    verify_headers, verify_data = DBUtil.run_query(verify_query, verify_desc, user, "sales", assignment)
    
    if verify_data and len(verify_data) > 0:
        row_count = int(verify_data[0][0])
        if row_count == 0:
            print(f"⚠ ERROR: Sale table has {row_count} rows - INSERT may have failed")
            return
    else:
        print("⚠ ERROR: Could not verify sale table - table may not exist")
        return

    # Create pivot table for sales database
    # Following professor's instruction: x is vertical (rows), y is horizontal (columns)
    # So product_name (x) becomes rows, store_location (y) becomes columns
    make_pivot_table(assignment, user, "sales", "sale", "product_name", "store_location", "num_sales")

    # Create pivot table for university database
    # x (rows) = name, y (columns) = dept_name
    make_pivot_table(assignment, user, "university", "instructor", "name", "dept_name", "salary")

    # Create pivot table for meta database
    # x (rows) = query_assn, y (columns) = query_db
    make_pivot_table(assignment, user, "meta", "query", "query_assn", "query_db", "query_dur")


if __name__ == "__main__":
    main()
