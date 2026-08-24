# # Database Systems (CSCI 331)
# # Winter 2026
# # DBUTIL Helper Class
# # Zohaib Cheema
#
#
#
#
# def main():
#     pass
#
# import time
# import pymysql
# import OutputUtil as ou
#
#
#
#
# def getPassword():
#     with open('pwd.txt', "r") as file:
#         return file.read().strip()
#
# def read_queries(file_name):
#     with open(file_name, "r") as file:
#         text = file.read()
#         raw_queries = text.split(';')
#         queries = []
#
#         for raw_query in raw_queries:
#             if '*/' in raw_query:
#                 desc, sql = raw_query.split('*/')
#                 desc = desc.replace('/*', '')
#             else:
#                 sql = raw_query
#                 desc = 'n/a'
#             if len(sql.strip()) > 5:
#                 queries.append([sql.strip(), desc.strip()])
#         return queries
#
# def read_and_run_queries(file_name, db, user, assignment):
#     queries = read_queries(file_name)
#     [queries.append(query) for query in add_analytics(assignment)]
#     # tables = get_tables_in_database(user, db, assignment)
#     # data_tables00 = show_tables(user, db, assignment)
#     # data_tables0 = desc_tables(tables, user, db, assignment)
#     data_tables1 = run_queries(queries, user, db, assignment)
#     # data_tables2 = get_assignment_summary(assignment)
#
#     file_name = f"Assignment{assignment}.html"
#     my_title = f"Assignment{assignment}"
#     data_tables = data_tables1 # delete later
#     # data_tables = data_tables00 + data_tables0 + data_tables1 + data_tables2
#     if len(data_tables) > 0:
#         ou.write_html_file_new(file_name, my_title, None, data_tables, True, None, True)
#
# def add_analytics(assn):
#     queries = []
#     sql1 = "SELECT query_assn AS assignment, COUNT(*) AS queries, MIN(query_dur) AS fastest, MAX(query_dur) AS slowest, ROUND(AVG(query_dur),4) AS average, MIN(query_ended) AS first, MAX(query_ended) AS last FROM meta.query GROUP BY query_assn"
#     desc1 = "get a summary table for all assignments"
#     queries.append([sql1, desc1])
#     sql2 = f"SELECT * FROM meta.query WHERE query_assn = '{assn}'"
#     desc2 = "Retrieve a query log for the current assignment"
#     queries.append([sql2, desc2])
#     return queries
#
#
#
# def run_queries(queries, user, db, assignment):
#     password = getPassword()
#     tables = []
#     conn = pymysql.connections.Connection(host="localhost", user="root", passwd=password, db=db)
#     for query in queries:
#         sql, desc = query
#         try:
#             start = time.time()
#             cursor = conn.cursor()
#             cursor.execute(sql)
#             end = time.time()
#             duration = end - start
#             rows = cursor.fetchall()
#             sql = sql.strip()                       # to get rid of any white space before or after the query
#             log_query(conn, sql, desc, db, len(rows), user, assignment, duration)
#             cmd = sql.split(' ')[0].upper()         # what is the first word in the query
#             if cmd in ["SELECT", "SHOW", "DESC"]:   # formatting headers etc. to formate data in html
#                 headers = [desc[0] for desc in cursor.description]
#                 data = [[str(col) for col in row] for row in rows] # getting data
#                 title = desc + "-----" + sql # description of query
#                 numeric = [all([data[row][col].replace('.', '').isnumeric() for row in range(len(data))]) for col in
#                            range(len(headers))]
#                 alignments = ["r" if numeric[i] else "l" for i in range(len(numeric))]
#                 types = ["N" if numeric[i] else "S" for i in range(len(numeric))]
#             else:
#                 title = desc
#                 headers = [cmd]
#                 data = [["NONE"]]
#                 tables.append([title, headers, ["S"], ["l"], data])
#
#                 alignments = ["l"] * len(headers) # left alignment
#                 types = ["S"] * len(headers)        # makes everything a string
#                 tables.append([title, headers, types, alignments, data])
#         except:
#             print("Error while running query", sql)  # gives error
#             conn.rollback()     # got to previous stats
#             conn.close()          # closing the database connection
#             return []
#     conn.commit()  # commit saves
#     conn.close()    # always essential
#     return tables
#
#
# def log_query(conn, query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur):
#     query_text = query_text.replace("'", "\\'")
#     query_text = query_desc.replace("'", "\\'")
#     query = f"INSERT into meta.query (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) \nvalues ('{query_text}', '{query_desc}', '{query_db}', {query_rows}, '{query_user}', '{query_assn}', {query_dur})"
#     # print(query)
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#
# def main():
#     user = "Zohaib"
#     db = "university"
#     assn = "03"
#     file_name = f"Assignment{assn}.html"
#     my_title = f"Queries for Assignment{assn}"
#     tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes", "teaches", "time_slot"]
#
#     sql = "SELECT id, name, dept_name from instructor"
#     desc = "get instructors from instructor table"
#     queries = [[sql.desc]]
#
#     for table in tables:
#         sql2 = f"DESC {table}"
#         desc2 = f"Show all columns in the table \"{table}\""
#         queries.append((sql2, desc2))
#
#         sql2a = f"SELECT * FROM {table}"
#         desc2a = f"Show all columns in the table \"{table}\""
#         queries.append((sql2a, desc2a))
#
#         sql2b = f"SELECT COUNT(*) as count_rows FROM {table}"
#         desc2b = f"Count the number of rows in the table \"{table}\""
#
#         output_tables = run_queries(queries, user, db, assn)
#         queries4 = []
#         sql4a = "SELECT id, name, ROUND(salary/12,2) AS monthly_salary FROM instructor"
#         desc4a = "Get instructors and their monthly salaries"
#         queries4.append((sql4a, desc4a))
#
#         sql4b = "SELECT name FROM instructor WHERE dept_name = 'Comp. Sci.' and salary > 70000"
#         desc4b = "To find all instructors in Comp. Sci. dept with salary greater than 70000"
#         queries4.append((sql4b, desc4b))
#
#         sql4c = "SELECT DISTINCT T.name FROM instructor AS T, instructor AS S WHERE T.salary > S.salary AND S.dept_name = 'Comp. Sci.’"
#         desc4c = "Find the names of all instructors who have a higher salary than some instructor in Comp. Sci"
#         queries4.append((sql4c, desc4c))
#
#         output_tables4 = runqueries(queries4, user, db, assn)
#         output_tables += output_tables4
#
#         sql5 = f"SELECT * FROM meta.query WHERE query_assn = '{assn}'"
#         desc5 = "Getting all queries for the current assignment"
#         queries5 = [[sql5, desc5]]
#         output_tables5 = run_queries(queries5, user, "meta", assn)
#         output_tables += output_tables5
#
#     # data_tables = run_queries(queries, db, assignment)
#     # if len(data_tables) > 0:
#
#     if len(output_tables) > 0:
#         ou.write_html_file_new(file_name, my_title, None, output_tables, True, None, True)
#
#
#
# import mysql.connector
# mydb = mysql.connector.connect()
# conn = mysql.connector.connect(host="localhost", user="root",passwd="password")








# Database Systems (CSCI 331)
# Winter 2026
# DBUTIL Helper Class
# Zohaib Cheema




def main():
    pass

import time
import pymysql
import json
import OutputUtil as ou




def getPassword():
    with open('pwd.txt', "r") as file:
        return file.read().strip()

def read_queries(file_name):
    with open(file_name, "r") as file:
        text = file.read()
        raw_queries = text.split(';')
        queries = []

        for raw_query in raw_queries:
            if '*/' in raw_query:
                desc, sql = raw_query.split('*/',1)
                desc = desc.replace('/*', '')
            else:
                sql = raw_query
                desc = 'n/a'
            if len(sql.strip()) > 5:
                queries.append([sql.strip(), desc.strip()])
        return queries

def read_and_run_queries(file_name, db, user, assignment):
    if not file_name:
        file_name = f"Assignment{assignment}.sql"
    queries = read_queries(file_name)
    [queries.append(query) for query in add_analytics(assignment)]
    # tables = get_tables_in_database(user, db, assignment)
    # data_tables00 = show_tables(user, db, assignment)
    # data_tables0 = desc_tables(tables, user, db, assignment)
    data_tables1 = run_queries(queries, user, db, assignment)
    # data_tables2 = get_assignment_summary(assignment)

    file_name = f"Assignment{assignment}.html"
    my_title = f"Assignment{assignment}"
    data_tables = data_tables1 # delete later
    # data_tables = data_tables00 + data_tables0 + data_tables1 + data_tables2
    if len(data_tables) > 0:
        ou.write_html_file_new(file_name, my_title, None, data_tables, True, None, True)

def add_analytics(assn):
    queries = []
    sql1 = "SELECT query_assn AS assignment, COUNT(*) AS queries, MIN(query_dur) AS fastest, MAX(query_dur) AS slowest, ROUND(AVG(query_dur),4) AS average, MIN(query_ended) AS first, MAX(query_ended) AS last FROM meta.`query` GROUP BY query_assn"
    desc1 = "get a summary table for all assignments"
    queries.append([sql1, desc1])
    sql2 = f"SELECT * FROM meta.`query` WHERE query_assn = '{assn}'"
    desc2 = "Retrieve a query log for the current assignment"
    queries.append([sql2, desc2])
    sql3 = "SELECT * FROM university.v_table_columns"
    desc3 = "Retreive a list of all tables and columns across my database"
    queries.append([sql3, desc3])
    sql4 = """SELECT query_assn, COUNT(CASE WHEN WEEKDAY(query_ended) = 0 THEN query_id END) as 'Monday', COUNT(CASE WHEN WEEKDAY(query_ended) = 1 THEN query_id END) as 'Tuesday', COUNT(CASE WHEN WEEKDAY(query_ended) = 2 THEN query_id END) as 'Wednesday', COUNT(CASE WHEN WEEKDAY(query_ended) = 3 THEN query_id END) as 'Thursday', COUNT(CASE WHEN WEEKDAY(query_ended) = 4 THEN query_id END) as 'Friday', COUNT(CASE WHEN WEEKDAY(query_ended) = 5 THEN query_id END) as 'Saturday', COUNT(CASE WHEN WEEKDAY(query_ended) = 6 THEN query_id END) as 'Sunday', COUNT(query_id) as 'Total_Per_Assignment' FROM meta.query GROUP BY query_assn UNION ALL SELECT 'Total_Per_day' as query_assn, COUNT(CASE WHEN WEEKDAY(query_ended) = 0 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 1 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 2 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 3 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 4 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 5 THEN query_id END), COUNT(CASE WHEN WEEKDAY(query_ended) = 6 THEN query_id END), COUNT(query_id) FROM meta.query"""
    desc4 = "Make a pivot table of the query table by day"
    queries.append([sql4, desc4])
    return queries




def run_queries(queries, user, db, assignment, add_stats=False, frmt=None):
    password = getPassword()
    tables = []
    conn = pymysql.connections.Connection(host="localhost", user="root", passwd=password, db=db)
    for query in queries:
        sql, desc = query
        try:
            start = time.time()
            cursor = conn.cursor()
            cursor.execute(sql)
            end = time.time()
            duration = end - start
            rows = cursor.fetchall()
            sql = sql.strip()                       # to get rid of any white space before or after the query
            log_query(conn, sql, desc, db, len(rows), user, assignment, duration)
            cmd = sql.split(' ')[0].upper()         # what is the first word in the query
            # MySQL exposes metadata for every statement that returns a result set,
            # including EXPLAIN. Checking cursor.description is more reliable than
            # maintaining a hard-coded list of SQL command names.
            if cursor.description is not None:
                headers = [desc[0] for desc in cursor.description]
                data = [[str(col) for col in row] for row in rows]  # getting data
                original_col_count = len(headers)
                if frmt in ["F", "V"]:
                    cursor_desc = cursor.description
                    add_formatted_data(frmt, cursor_desc, headers, data)
                title = desc + "-----" + sql  # description of query
                numeric = [all([data[row][col].replace('.', '').isnumeric() for row in range(len(data))]) for col in
                           range(original_col_count)]
                # The formatted column (ruler) is always a string
                if frmt in ["F", "V"]:
                    numeric.append(False)
                alignments = ["r" if numeric[i] else "l" for i in range(len(numeric))]
                types = ["N" if numeric[i] else "S" for i in range(len(numeric))]
                tables.append([title, headers, types, alignments, data])
                if add_stats:
                    stat_cols = [j for j in range(len(numeric)) if numeric[j]]
                    if len(data) > 0 and len(stat_cols) > 0:  # Only call add_stats if there's data and numeric columns
                        try:
                            ou.add_stats(data, stat_cols, 0, 3, True)
                        except (TypeError, ValueError):
                            # Skip stats if there's a type error (e.g., mixed string/numeric data)
                            pass
            else:
                title = desc
                headers = [cmd]
                data = [["Statement executed successfully"]]

                alignments = ["l"] * len(headers) # left alignment
                types = ["S"] * len(headers)        # makes everything a string
                tables.append([title, headers, types, alignments, data])
        except Exception as e:
            print("Error while running query", sql[:100] if len(sql) > 100 else sql)  # gives error
            print(f"Error details: {e}")
            conn.rollback()     # got to previous stats
            # Continue to next query instead of stopping
            continue
    conn.commit()  # commit saves
    conn.close()    # always essential
    return tables


def log_query(conn, query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur):
    query_text = query_text.replace("'", "\\'")
    query_desc = query_desc.replace("'", "\\'")
    query = f"INSERT into meta.`query` (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) \nvalues ('{query_text}', '{query_desc}', '{query_db}', {query_rows}, '{query_user}', '{query_assn}', {query_dur})"
    # print(query)
    cursor = conn.cursor()
    cursor.execute(query)


# Define a function get_ruler_for_html(length) that will create a "ruler" used to measure the positions and total space
def get_ruler_for_html(length):
    ruler1 = "".join([str(10*i).rjust(10, ' ') for i in range(1, 2+int(length/10))])
    ruler1 = ruler1.replace(" ", "&nbsp;")
    ruler2 = "0123456789" * (1 + int(length/10))
    return ruler1 + "<br>" + ruler2


def add_formatted_data(frmt, cursor_desc, headers, data):
    headers.append(("Fixed" if frmt == "F" else "Variable") + "-Length Format")
    col_widths = [desc[3] for desc in cursor_desc]
    for row in data:
        if frmt == "F":
            record = "".join([str(row[i]).ljust(col_widths[i], " ") for i in range(len(col_widths))])
            record = record.replace(" ", "&nbsp;")
        else:
            record = "|".join([str(row[i]) for i in range(len(col_widths))])
        ruler = "<tt>" + get_ruler_for_html(sum(col_widths)) + "<br>" + record + "</tt>"
        row.append(ruler)


def main():
    user = "Zohaib"
    db = "university"
    assn = "03"
    file_name = f"Assignment{assn}.html"
    my_title = f"Queries for Assignment{assn}"
    tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes", "teaches", "time_slot"]

    sql = "SELECT id, name, dept_name from instructor"
    desc = "get instructors from instructor table"
    queries = [[sql.desc]]

    for table in tables:
        sql2 = f"DESC {table}"
        desc2 = f"Show all columns in the table \"{table}\""
        queries.append((sql2, desc2))

        sql2a = f"SELECT * FROM {table}"
        desc2a = f"Show all columns in the table \"{table}\""
        queries.append((sql2a, desc2a))

        sql2b = f"SELECT COUNT(*) as count_rows FROM {table}"
        desc2b = f"Count the number of rows in the table \"{table}\""

        output_tables = run_queries(queries, user, db, assn)
        queries4 = []
        sql4a = "SELECT id, name, ROUND(salary/12,2) AS monthly_salary FROM instructor"
        desc4a = "Get instructors and their monthly salaries"
        queries4.append((sql4a, desc4a))

        sql4b = "SELECT name FROM instructor WHERE dept_name = 'Comp. Sci.' and salary > 70000"
        desc4b = "To find all instructors in Comp. Sci. dept with salary greater than 70000"
        queries4.append((sql4b, desc4b))

        sql4c = "SELECT DISTINCT T.name FROM instructor AS T, instructor AS S WHERE T.salary > S.salary AND S.dept_name = 'Comp. Sci.’"
        desc4c = "Find the names of all instructors who have a higher salary than some instructor in Comp. Sci"
        queries4.append((sql4c, desc4c))

        output_tables4 = runqueries(queries4, user, db, assn)
        output_tables += output_tables4

        sql5 = f"SELECT * FROM meta.`query` WHERE query_assn = '{assn}'"
        desc5 = "Getting all queries for the current assignment"
        queries5 = [[sql5, desc5]]
        output_tables5 = run_queries(queries5, user, "meta", assn)
        output_tables += output_tables5

    # data_tables = run_queries(queries, db, assignment)
    # if len(data_tables) > 0:

    if len(output_tables) > 0:
        ou.write_html_file_new(file_name, my_title, None, output_tables, True, None, True)



# import mysql.connector
# mydb = mysql.connector.connect()
# conn = mysql.connector.connect(host="localhost", user="root",passwd=getPassword())


# Assignment 07 Functions

def is_numeric(s):
    """Check if a string represents a number"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def run_query(sql, desc, user, db, assignment, skip_log=False):
    """
    Simplified version of run_queries for Assignment 07.
    Executes a single query and returns headers and data.
    skip_log: If True, skip logging (useful for large INSERT queries that exceed query_text column size)
    """
    password = getPassword()
    headers = []
    data = []
    conn = pymysql.connections.Connection(host="localhost", user="root", passwd=password, db=db)
    try:
        start = time.time()
        cursor = conn.cursor()
        sql = sql.strip()
        cursor.execute(sql)
        end = time.time()
        duration = end - start
        rows = cursor.fetchall()
        if not skip_log:
            # Truncate very long queries for logging (meta.query.query_text has size limit)
            sql_for_log = sql if len(sql) < 1000 else sql[:997] + "..."
            try:
                log_query(conn, sql_for_log, desc, db, len(rows), user, assignment, duration)
            except Exception:
                # If logging fails (e.g., query too long), continue without logging
                pass
        if cursor.description is not None:
            headers = [desc[0] for desc in cursor.description]
            data = [[str(col) for col in row] for row in rows]
        conn.commit()
    except Exception as e:
        print("Error while running query", sql[:100] if len(sql) > 100 else sql)
        print(e)
        conn.rollback()
        conn.close()
        return [], []
    conn.close()
    return headers, data


def pivot_table(assn, user, db, table, column_x, column_y, column_val):
    """
    Build a pivot table for an arbitrary table and columns.
    Following professor's instruction: x is vertical (rows), y is horizontal (columns).
    Returns a table in the format [title, headers, types, alignments, data]
    """
    # Get all distinct values of column_y from table for pivot table (these become columns/horizontal)
    query = f"SELECT DISTINCT {column_y} FROM {table}"
    desc = f"Get all distinct values of {column_y} from {table} for pivot table"
    headers, data = run_query(query, desc, user, db, assn)
    
    # Check if we have data to pivot
    if not data or len(data) == 0:
        # Try to get a count to see if table exists and has any data
        count_query = f"SELECT COUNT(*) as total_rows FROM {table}"
        count_headers, count_data = run_query(count_query, f"Check if {table} has data", user, db, assn)
        if count_data and len(count_data) > 0 and int(count_data[0][0]) > 0:
            # Table has data but column_y might have NULLs or empty values
            error_msg = f"Table {table} has {count_data[0][0]} rows but no distinct values in {column_y}"
        else:
            error_msg = f"No data found in table {table} for pivot table {column_x} vs {column_y}"
        # Return empty table structure
        return [error_msg, [column_x], ["S"], ["l"], []]
    
    # Build the pivot table query
    case_statements = []
    for row in data:
        value = str(row[0])
        # Replace dots and spaces with underscores for column names
        col_name = value.replace(".", "_").replace(" ", "_")
        case_statements.append(f"SUM(CASE WHEN {column_y} = '{value}' THEN {column_val} ELSE 0 END) AS {col_name}")
    
    # column_x becomes rows (vertical), column_y values become columns (horizontal)
    query = f"SELECT {column_x}, " + ",\n".join(case_statements) + f" FROM {table} GROUP BY {column_x}"
    desc = f"Build a pivot table for {column_x} vs {column_y} for {table}"
    headers, data = run_query(query, desc, user, db, assn)
    
    # Check if we have result data
    if not data or len(data) == 0:
        return [desc, headers if headers else [column_x], ["S"], ["l"], []]
    
    # Determine numeric columns
    numeric = [all([is_numeric(str(data[i][j])) for i in range(len(data))]) for j in range(len(data[0]))]
    types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    
    table_result = [desc, headers, types, alignments, data]
    return table_result


# [2a] Create a Python function to_csv(headers, data) that converts the headers and data into CSV format
def to_csv(headers, data):
    s_headers = ','.join(headers)
    s_data = '\n'.join([",".join([str(col) for col in row]) for row in data])
    return s_headers + "\n" + s_data
