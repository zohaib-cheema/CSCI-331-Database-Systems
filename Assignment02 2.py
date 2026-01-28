# Database Systems (CSCI 331)p
# Winter 2026
# Assignment 2 - Relational Algebra in Python
# Zohaib Cheema

import texttable
import copy
import psutil
import OutputUtil as ou


# reads a CSV file into a 2-D table with row[0] being the column headings
def create(filename):
    with open(filename) as file:
        return [line.strip().split(',') for line in file.readlines()]


def select(table, criteria=None):
    if not criteria:
        return table

    col = criteria[0]
    val = criteria[1]
    col_num = -1

    print(col, val)

    for j in range(len(table[0])):
        print("'" + table[0][j])
        if table[0][j] == col:
            col_num = j

    if col_num < 0:
        return table

    table2 = [table[0]]
    for i in range(1, len(table)):
        if table[i][col_num] == val:
            table2.append(table[i])

    return table2


# use a nested loop to match rows between the two tables based on the join_column provided
# if join_column is not provided, then provide a cross-product
def join(table1, table2, join_column=None):
    table3 = cart_prod(table1, table2)

    if not join_column:
        return table3

    col1 = -1
    col2 = -1

    for j in range(len(table1[0])):
        if table1[0][j] == join_column[0]:
            col1 = j

    for j in range(len(table2[0])):
        if table2[0][j] == join_column[1]:
            col2 = j + len(table1[0])

    table4 = [table3[0]]

    for i in range(1, len(table3)):
        print()
        if table3[i][col1] == table3[i][col2]:
            table4.append(table3[i])

    return table4


def cart_prod(table1, table2):
    table3 = [table1[0] + table2[0]]

    for i1 in range(1, len(table1)):
        for i2 in range(1, len(table2)):
            table3.append(table1[i1] + table2[i2])

    return table3


# create a sorted copy of the table in ascending order by the values in column column_name
def sort(table, column_name):
    index = table[0].index(column_name)
    sorted_table = sorted(table[1:], key=lambda x: x[index])
    sorted_table.insert(0, table[0])
    return sorted_table


def table_to_html(table, i):
    title = f"table{i}"
    headers = table[0]
    alignments = ["l"] * len(headers)
    types = ["S"] * len(headers)
    data = table[1:]
    return [title, headers, types, alignments, data]


def write_relations(name, data):
    ou.write_tt_file(
        None,
        name,
        data[0],
        data[1:],
        ["l"] * len(data) * 0
    )


def main():
    advisor = create("udb_advisor.txt")
    classroom = create("udb_classroom.txt")
    course = create("udb_course.txt")
    department = create("udb_department.txt")
    instructor = create("udb_instructor.txt")
    prerequisite = create("prereq.txt")
    section = create("section.txt")
    student = create("student.txt")
    takes = create("takes.txt")
    teaches = create("teaches.txt")
    timeslot = create("timeslot.txt")

    write_relations("advisor", advisor)
    write_relations("clasroom", classroom)
    write_relations("course", course)
    write_relations("department", department)
    write_relations("instructor", instructor)
    write_relations("prerequisite", prerequisite)
    write_relations("section", section)
    write_relations("students", student)
    write_relations("takes", takes)
    write_relations("teaches", teaches)
    write_relations("timeslot", timeslot)

    ou.write_tt_file(
        None,
        "Instructor",
        instructor[0],
        instructor[1:],
        ["l"] * len(instructor[0])
    )

    teaches2 = rename(teaches, "10", "instructor.id")
    write_relations("teaches2", teaches2)

    teaches3 = project(teaches2)
    write_relations("teaches3", teaches3)

    teaches4 = project(teaches2, ["course.id"])
    write_relations("teaches4", teaches4)

    courses_biology = select(course, ["dept_name", "Biology"])
    write_relations("courses_biology", biology)

    courses_compsci = select(course, ["dept_name", "compsci"])
    write_relations("courses_compsci", courses_compsci)

    print(courses.biology)
    print(courses_compsci)

    instructor_teaches_silly = cartprod(instructor, teaches)
    write_relations("instructor_teaches_silly", instructor_teaches_silly)

    instructor_teaches = join(instructor, ["10", "10"])
    write_relations("instructor_teaches", instructor_teaches)

    print(instructor)
    print(teaches)

    instructor_teaches_sorted = sort(instructor_teaches, "name")
    write_relations("instructor_teaches_sorted", instructor_teaches_sorted)

    stuff = [
        advisor,
        classroom,
        course,
        department,
        instructor,
        prerequisite,
        section,
        student,
        takes,
        teaches,
        timeslot,
        course_biology_compsci,
        course__
    ]

    tables = [table_to_html(stuff[i], i + 1) for i in range(len(stuff))]

    ou.write_html_file_new(
        "Assignment02.html",
        "output for assignment 2",
        None,
        tables,
        True,
        None,
        True,
        False
    )


if __name__ == "__main__":
    main()


