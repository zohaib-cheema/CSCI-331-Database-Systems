# Database Systems (CSCI 331)
# Winter 2026
# Assignment 3 - SQL & Programming Language
# Zohaib Cheema


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
# import mysql.connector
# mydb = mysql.connector.connect()
#
# conn = mysql.connector.connect(host="localhost", user="username",passwd="password")
#
#
# if __name__ == "__main__":
#     main()

# Database Systems (CSCI 331)
# Winter 2026
# Assignment 3 - SQL & Programming Language
# Zohaib Cheema


def main():
    pass

import time
import pymysql
import OutputUtil as ou




def getPassword():
    with open('pwd.txt', "r") as file:
        return file.read().strip()



def run_queries(queries, user, db, assignment):
    password = getPassword()
    tables_out = []
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
            if cmd in ["SELECT", "SHOW", "DESC"]:   # formatting headers etc. to formate data in html
                headers = [d[0] for d in cursor.description]
                data = [[str(col) for col in row] for row in rows] # getting data
                title = desc + "-----" + sql # description of query
                alignments = ["l"] * len(headers) # left alignment
                types = ["S"] * len(headers)        # makes everything a string
                tables_out.append([title, headers, types, alignments, data])
                ou.write_tt_file(None,title,headers,data,alignments)
        except:
            print("Error while running query", sql)  # gives error
            conn.rollback()     # got to previous stats
            conn.close()          # closing the database connection
            return []
    conn.commit()  # commit saves
    conn.close()    # always essential
    return tables_out

def log_query(conn, query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur):
    query_text = query_text.replace("'", "\\'")
    query_desc = query_desc.replace("'", "\\'")
    query = f"INSERT into meta.`query` (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) \nvalues ('{query_text}', '{query_desc}', '{query_db}', {query_rows}, '{query_user}', '{query_assn}', {query_dur})"
    # print(query)
    cursor = conn.cursor()
    cursor.execute(query)


def main():
    user = "Zohaib"
    db = "university"
    assn = "03"
    file_name = f"Assignment{assn}.html"
    my_title = f"Queries for Assignment{assn}"
    tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes", "teaches", "time_slot"]

    sql = "SELECT id, name, dept_name from instructor"
    desc = "Get instructors from instructor table"
    queries = [(sql, desc)]

    for table in tables:
        sql2 = f"DESC {table}"
        desc2 = f"Show all columns in the table \"{table}\""
        queries.append((sql2, desc2))

        sql2a = f"SELECT * FROM {table}"
        desc2a = f"Show all columns in the table \"{table}\""
        queries.append((sql2a, desc2a))

        sql2b = f"SELECT COUNT(*) as count_rows FROM {table}"
        desc2b = f"Count the number of rows in the table \"{table}\""
        queries.append((sql2b, desc2b))


    output_tables = run_queries(queries, user, db, assn)

    queries4 = []
    sql4a = "SELECT id, name, ROUND(salary/12,2) AS monthly_salary FROM instructor"
    desc4a = "Get instructors and their monthly salaries"
    queries4.append((sql4a, desc4a))

    sql4b = "SELECT name FROM instructor WHERE dept_name = 'Comp. Sci.' and salary > 70000"
    desc4b = "To find all instructors in Comp. Sci. dept with salary greater than 70000"
    queries4.append((sql4b, desc4b))

    sql4c = "SELECT DISTINCT T.name FROM instructor AS T, instructor AS S WHERE T.salary > S.salary AND S.dept_name = 'Comp. Sci.'"
    desc4c = "Find the names of all instructors who have a higher salary than some instructor in Comp. Sci"
    queries4.append((sql4c, desc4c))

    output_tables4 = run_queries(queries4, user, db, assn)
    output_tables += output_tables4

    sql5 = f"SELECT * FROM meta.`query` WHERE query_assn = '{assn}'"
    desc5 = "Getting all queries for the current assignment"
    queries5 = [(sql5, desc5)]
    output_tables5 = run_queries(queries5, user, "meta", assn)
    output_tables += output_tables5

    if len(output_tables) > 0:
        ou.write_html_file_new(file_name, my_title, None, output_tables, True, None, True)


if __name__ == "__main__":
    main()