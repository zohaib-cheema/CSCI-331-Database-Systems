# Database Systems CSCI 331
# Winter 2026
# Assignment 2 - Relational Algebra in Python
# Zohaib Cheema

import copy
import texttable
import OutputUtil as ou


def create(filename):
    table = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if line == "":
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 1 and parts[0] == "":
                continue
            table.append(parts)
    return table


def display(table, title=None):
    if title:
        print("\n" + title)

    headers = table[0]
    data = table[1:]
    rows = [headers] + data

    tt = texttable.Texttable(0)
    tt.set_cols_align(["l"] * len(headers))
    tt.add_rows(rows, header=True)
    print(tt.draw())


def rename(table, old_name, new_name):
    table2 = copy.deepcopy(table)
    for i in range(len(table2[0])):
        if table2[0][i] == old_name:
            table2[0][i] = new_name
            break
    return table2


def project(table, column_names=["*"]):
    if column_names == ["*"]:
        return copy.deepcopy(table)

    headers = table[0]
    idxs = []
    for col in column_names:
        if col in headers:
            idxs.append(headers.index(col))

    out = [[headers[i] for i in idxs]]
    for row in table[1:]:
        out.append([row[i] for i in idxs])
    return out


def select(table, criteria=None):
    if not criteria:
        return copy.deepcopy(table)

    col, val = criteria
    if col not in table[0]:
        return copy.deepcopy(table)

    col_num = table[0].index(col)

    table2 = [table[0]]
    for i in range(1, len(table)):
        if table[i][col_num] == val:
            table2.append(table[i])

    return table2


def union(results1, results2):
    headers = results1[0]
    out = [headers]

    seen = set()
    for r in results1[1:]:
        t = tuple(r)
        if t not in seen:
            seen.add(t)
            out.append(r)

    for r in results2[1:]:
        t = tuple(r)
        if t not in seen:
            seen.add(t)
            out.append(r)

    return out


def join(table1, table2, join_column=None):
    table3 = cart_prod(table1, table2)

    if not join_column:
        return table3

    if isinstance(join_column, str):
        left_col = join_column
        right_col = join_column
    else:
        left_col, right_col = join_column

    col1 = -1
    col2 = -1

    for j in range(len(table1[0])):
        if table1[0][j] == left_col:
            col1 = j

    for j in range(len(table2[0])):
        if table2[0][j] == right_col:
            col2 = j + len(table1[0])

    if col1 < 0 or col2 < 0:
        return table3

    table4 = [table3[0]]
    for i in range(1, len(table3)):
        if table3[i][col1] == table3[i][col2]:
            table4.append(table3[i])

    return table4


def cart_prod(table1, table2):
    table3 = [table1[0] + table2[0]]

    for i1 in range(1, len(table1)):
        for i2 in range(1, len(table2)):
            table3.append(table1[i1] + table2[i2])

    return table3


def sort(table, column_name):
    if column_name not in table[0]:
        return copy.deepcopy(table)

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


def write_relations(name, data, file_name=None):
    headers = data[0]
    rows = data[1:]
    alignment = ["l"] * len(headers)

    fixed = []
    for r in rows:
        if len(r) < len(headers):
            fixed.append(r + [""] * (len(headers) - len(r)))
        else:
            fixed.append(r[:len(headers)])

    ou.write_tt_file(file_name, name, headers, fixed, alignment)


def main():
    advisor = create("udb_advisor.txt")
    classroom = create("udb_classroom.txt")
    course = create("udb_course.txt")
    department = create("udb_department.txt")
    instructor = create("udb_instructor.txt")
    prereq = create("udb_prereq.txt")
    section = create("udb_section.txt")
    student = create("udb_student.txt")
    takes = create("udb_takes.txt")
    teaches = create("udb_teaches.txt")
    timeslot = create("udb_timeslot.txt")

    write_relations("advisor", advisor)
    write_relations("classroom", classroom)
    write_relations("course", course)
    write_relations("department", department)
    write_relations("instructor", instructor)
    write_relations("prereq", prereq)
    write_relations("section", section)
    write_relations("student", student)
    write_relations("takes", takes)
    write_relations("teaches", teaches)
    write_relations("timeslot", timeslot)

    # Ten relational algebra expressions

    # (1) rename instructor.ID -> instructor_id (example)
    instructor2 = rename(instructor, "ID", "instructor_id")

    # (2) instructor(name, dept_name)
    instructor3 = project(instructor, ["name", "dept_name"])

    # (3) courses in Biology
    courses_biology = select(course, ("dept_name", "Biology"))

    # (4) courses in Comp. Sci.
    courses_cs = select(course, ("dept_name", "Comp. Sci."))

    # (5) Biology U CompSci, projecting common cols first
    bio_proj = project(courses_biology, ["course_id", "title", "dept_name"])
    cs_proj = project(courses_cs, ["course_id", "title", "dept_name"])
    course_bio_cs = union(bio_proj, cs_proj)

    # (6) join instructor teaches on ID
    instr_teaches = join(instructor, teaches, "ID")

    # (7) join: (instructor teaches) course on course_id, then projecting useful columns
    instr_teaches_course = join(instr_teaches, course, "course_id")
    instr_teaches_course_proj = project(instr_teaches_course, ["name", "title", "semester", "year"])

    # (8) select: failed takes (grade F)
    failed = select(takes, ("grade", "F"))

    # (9) join: failed student on ID, then course on course_id, project
    failed_student = join(failed, student, "ID")
    failed_full = join(failed_student, course, "course_id")
    failed_proj = project(failed_full, ["name", "course_id", "title", "grade"])

    # (10) sort: student sorted by name
    student_sorted = sort(student, "name")

    out_file = "Assignment02.txt"
    write_relations("A) instructor2 (rename ID -> instructor_id)", instructor2, out_file)
    # append the rest manually (simple append)
    with open(out_file, "a", encoding="utf-8") as f:
        pass

    def append_table_to_txt(title, tbl):
        with open(out_file, "a", encoding="utf-8") as f:
            # rebuild a texttable drawing
            headers = tbl[0]
            data = tbl[1:]
            rows = [headers] + data
            tt = texttable.Texttable(0)
            tt.set_cols_align(["l"] * len(headers))
            tt.add_rows(rows, header=True)
            f.write("\n" + title + "\n")
            f.write(tt.draw() + "\n\n")

    append_table_to_txt("1) instructor3 = project(instructor, [name, dept_name])", instructor3)
    append_table_to_txt("2) courses_biology = select(course, (dept_name, Biology))", courses_biology)
    append_table_to_txt("3) courses_cs = select(course, (dept_name, Comp. Sci.))", courses_cs)
    append_table_to_txt("4) course_bio_cs = union(bio_proj, cs_proj)", course_bio_cs)
    append_table_to_txt("5) instr_teaches = join(instructor, teaches, ID)", instr_teaches)
    append_table_to_txt("6) instr_teaches_course_proj", instr_teaches_course_proj)
    append_table_to_txt("7) failed = select(takes, (grade, F))", failed)
    append_table_to_txt("8) failed_proj (failed students + course title)", failed_proj)
    append_table_to_txt("9) student_sorted = sort(student, name)", student_sorted)

    print("Wrote output file Assignment02.txt")

    stuff = [instructor2,instructor3,courses_biology,courses_cs,course_bio_cs,instr_teaches,instr_teaches_course_proj,failed,failed_proj,student_sorted]

    tables = [table_to_html(stuff[i], i + 1) for i in range(len(stuff))]

    ou.write_html_file_new(
        "Assignment02.html","Output for Assignment 02",None, tables,True,"mystyle.css",True,False)


if __name__ == "__main__":
    main()






