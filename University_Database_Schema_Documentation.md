# University Database Schema Documentation
## Based on Provided udb_*.txt Files

This document describes the University Database schema as provided in the udb_*.txt data files.

---

## 1. udb_student.txt → student Table

**Columns**:
- `ID` (VARCHAR/STRING): Student identifier (Primary Key)
- `name` (VARCHAR/STRING): Student name
- `dept_name` (VARCHAR/STRING): Department name (Foreign Key to department.dept_name)
- `tot_cred` (INTEGER): Total credits earned

**Total Records**: 13 students

**Complete Data**:
```
ID: 00128, name: Zhang, dept_name: Comp. Sci., tot_cred: 102
ID: 12345, name: Shankar, dept_name: Comp. Sci., tot_cred: 32
ID: 19991, name: Brandt, dept_name: History, tot_cred: 80
ID: 23121, name: Chavez, dept_name: Finance, tot_cred: 110
ID: 44553, name: Peltier, dept_name: Physics, tot_cred: 56
ID: 45678, name: Levy, dept_name: Physics, tot_cred: 46
ID: 54321, name: Williams, dept_name: Comp. Sci., tot_cred: 54
ID: 55739, name: Sanchez, dept_name: Music, tot_cred: 38
ID: 70557, name: Snow, dept_name: Physics, tot_cred: 0
ID: 76543, name: Brown, dept_name: Comp. Sci., tot_cred: 58
ID: 76653, name: Aoi, dept_name: Elec. Eng., tot_cred: 60
ID: 98765, name: Bourikas, dept_name: Elec. Eng., tot_cred: 98
ID: 98988, name: Tanaka, dept_name: Biology, tot_cred: 120
```

**Department Distribution**: Comp. Sci. (5 students), Physics (3), Elec. Eng. (2), History (1), Finance (1), Music (1), Biology (1)

**Relationships**:
- Related to `takes` table via `ID` (one student can take many courses)
- Related to `advisor` table via `ID` (one student can have one advisor)

---

## 2. udb_instructor.txt → instructor Table

**Columns**:
- `ID` (VARCHAR/STRING): Instructor identifier (Primary Key)
- `name` (VARCHAR/STRING): Instructor name
- `dept_name` (VARCHAR/STRING): Department name (Foreign Key to department.dept_name)
- `salary` (INTEGER): Annual salary

**Total Records**: 13 instructors

**Complete Data**:
```
ID: 10101, name: Srinivasan, dept_name: Comp. Sci., salary: 65000
ID: 12121, name: Wu, dept_name: Finance, salary: 90000
ID: 15151, name: Mozart, dept_name: Music, salary: 40000
ID: 22222, name: Einstein, dept_name: Physics, salary: 95000
ID: 32343, name: El Said, dept_name: History, salary: 60000
ID: 33456, name: Gold, dept_name: Physics, salary: 87000
ID: 45565, name: Katz, dept_name: Comp. Sci., salary: 75000
ID: 58583, name: Califieri, dept_name: History, salary: 62000
ID: 76543, name: Singh, dept_name: Finance, salary: 80000
ID: 76766, name: Crick, dept_name: Biology, salary: 72000
ID: 83821, name: Brandt, dept_name: Comp. Sci., salary: 92000
ID: 98345, name: Kim, dept_name: Elec. Eng., salary: 80000
```

**Salary Range**: $40,000 - $95,000

**Department Distribution**: Comp. Sci. (3), Physics (2), Finance (2), History (2), Music (1), Biology (1), Elec. Eng. (1)

**Relationships**:
- Related to `teaches` table via `ID` (one instructor can teach many course sections)
- Related to `advisor` table via `ID` (one instructor can advise many students)

---

## 3. udb_course.txt → course Table

**Columns**:
- `course_id` (VARCHAR/STRING): Course identifier (Primary Key)
- `title` (VARCHAR/STRING): Course title
- `dept_name` (VARCHAR/STRING): Department name (Foreign Key to department.dept_name)
- `credits` (INTEGER): Credit hours

**Total Records**: 13 courses

**Complete Data**:
```
course_id: BIO-101, title: Intro. to Biology, dept_name: Biology, credits: 4
course_id: BIO-301, title: Genetics, dept_name: Biology, credits: 4
course_id: BIO-399, title: Computational Biology, dept_name: Biology, credits: 3
course_id: CS-101, title: Intro. to Computer Science, dept_name: Comp. Sci., credits: 4
course_id: CS-190, title: Game Design, dept_name: Comp. Sci., credits: 4
course_id: CS-315, title: Robotics, dept_name: Comp. Sci., credits: 3
course_id: CS-319, title: Image Processing, dept_name: Comp. Sci., credits: 3
course_id: CS-347, title: Database System Concepts, dept_name: Comp. Sci., credits: 3
course_id: EE-181, title: Intro. to Digital Systems, dept_name: Elec. Eng., credits: 3
course_id: FIN-201, title: Investment Banking, dept_name: Finance, credits: 3
course_id: HIS-351, title: World History, dept_name: History, credits: 3
course_id: MU-199, title: Music Video Production, dept_name: Music, credits: 3
course_id: PHY-101, title: Physical Principles, dept_name: Physics, credits: 4
```

**Credit Distribution**: 3 credits (9 courses), 4 credits (4 courses)

**Department Distribution**: Comp. Sci. (5), Biology (3), Physics (1), Elec. Eng. (1), Finance (1), History (1), Music (1)

**Relationships**:
- Related to `prereq` table via `course_id` (one course can have multiple prerequisites)
- Related to `takes` table via `course_id` (one course can be taken by many students)
- Related to `section` table via `course_id` (one course can have multiple sections)
- Related to `teaches` table via `course_id` (one course can be taught by multiple instructors)

---

## 4. udb_takes.txt → takes Table

**Columns**:
- `ID` (VARCHAR/STRING): Student ID (Foreign Key to student.ID)
- `course_id` (VARCHAR/STRING): Course ID (Foreign Key to course.course_id)
- `sec_id` (INTEGER): Section ID
- `semester` (VARCHAR/STRING): Semester (Fall, Spring, Summer)
- `year` (INTEGER): Year
- `grade` (VARCHAR/STRING or NULL): Letter grade received

**Total Records**: 22 enrollment records

**Complete Data**:
```
ID: 00128, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: A
ID: 00128, course_id: CS-347, sec_id: 1, semester: Fall, year: 2017, grade: A-
ID: 12345, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: C
ID: 12345, course_id: CS-190, sec_id: 2, semester: Spring, year: 2017, grade: A
ID: 12345, course_id: CS-315, sec_id: 1, semester: Spring, year: 2018, grade: A
ID: 12345, course_id: CS-347, sec_id: 1, semester: Fall, year: 2017, grade: A
ID: 19991, course_id: HIS-351, sec_id: 1, semester: Spring, year: 2018, grade: B
ID: 23121, course_id: FIN-201, sec_id: 1, semester: Spring, year: 2018, grade: C+
ID: 44553, course_id: PHY-101, sec_id: 1, semester: Fall, year: 2017, grade: B-
ID: 45678, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: F
ID: 45678, course_id: CS-101, sec_id: 1, semester: Spring, year: 2018, grade: B+
ID: 45678, course_id: CS-319, sec_id: 1, semester: Spring, year: 2018, grade: B
ID: 54321, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: A-
ID: 54321, course_id: CS-190, sec_id: 2, semester: Spring, year: 2017, grade: B+
ID: 55739, course_id: MU-199, sec_id: 1, semester: Spring, year: 2018, grade: A-
ID: 76543, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: A
ID: 76543, course_id: CS-319, sec_id: 2, semester: Spring, year: 2018, grade: A
ID: 76653, course_id: EE-181, sec_id: 1, semester: Spring, year: 2017, grade: C
ID: 98765, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, grade: C-
ID: 98765, course_id: CS-315, sec_id: 1, semester: Spring, year: 2018, grade: B
ID: 98988, course_id: BIO-101, sec_id: 1, semester: Summer, year: 2017, grade: A
ID: 98988, course_id: BIO-301, sec_id: 1, semester: Summer, year: 2018, grade: null
```

**Grade Values Found**: A, A-, B+, B, B-, C+, C, C-, F, null

**Note**: One record has `grade: null` (BIO-301, student 98988, Summer 2018)

**Semester/Year Distribution**: Fall 2017 (8 records), Spring 2017 (3 records), Spring 2018 (9 records), Summer 2017 (1 record), Summer 2018 (1 record)

**Relationships**:
- Foreign key to `student` table via `ID`
- Foreign key to `course` table via `course_id`
- Foreign key to `section` table via (`course_id`, `sec_id`, `semester`, `year`)

---

## 5. udb_prereq.txt → prereq Table

**Columns**:
- `course_id` (VARCHAR/STRING): Course ID that requires a prerequisite (Foreign Key to course.course_id)
- `prereq_id` (VARCHAR/STRING): Prerequisite course ID (Foreign Key to course.course_id)

**Total Records**: 7 prerequisite relationships

**Complete Data**:
```
course_id: BIO-301, prereq_id: BIO-101
course_id: BIO-399, prereq_id: BIO-101
course_id: CS-190, prereq_id: CS-101
course_id: CS-315, prereq_id: CS-101
course_id: CS-319, prereq_id: CS-101
course_id: CS-347, prereq_id: CS-101
course_id: EE-181, prereq_id: PHY-101
```

**Prerequisite Pattern**:
- CS-101 is a prerequisite for: CS-190, CS-315, CS-319, CS-347 (4 courses)
- BIO-101 is a prerequisite for: BIO-301, BIO-399 (2 courses)
- PHY-101 is a prerequisite for: EE-181 (1 course)

**Relationships**:
- Self-referential relationship on `course` table
- Both `course_id` and `prereq_id` are foreign keys to `course.course_id`

---

## 6. udb_advisor.txt → advisor Table

**Columns**:
- `s_ID` (VARCHAR/STRING): Student ID (Foreign Key to student.ID)
- `i_ID` (VARCHAR/STRING): Instructor ID (Foreign Key to instructor.ID)

**Total Records**: 9 advisor-student relationships

**Complete Data**:
```
s_ID: 00128, i_ID: 45565
s_ID: 12345, i_ID: 10101
s_ID: 23121, i_ID: 76543
s_ID: 44553, i_ID: 22222
s_ID: 45678, i_ID: 22222
s_ID: 76543, i_ID: 45565
s_ID: 76653, i_ID: 98345
s_ID: 98765, i_ID: 98345
s_ID: 98988, i_ID: 76766
```

**Advisor Distribution**:
- Instructor 45565 (Katz, Comp. Sci.) advises: 2 students (00128, 76543)
- Instructor 22222 (Einstein, Physics) advises: 2 students (44553, 45678)
- Instructor 98345 (Kim, Elec. Eng.) advises: 2 students (76653, 98765)
- Other instructors advise: 1 student each (10101, 76543, 76766)

**Note**: 4 students (19991, 54321, 55739, 70557) do not have advisors listed in this table.

**Relationships**:
- Foreign key to `student` table via `s_ID`
- Foreign key to `instructor` table via `i_ID`
- Many-to-many relationship: one student has one advisor, one instructor can advise multiple students

---

## 7. udb_section.txt → section Table

**Columns**:
- `course_id` (VARCHAR/STRING): Course ID (Foreign Key to course.course_id)
- `sec_id` (INTEGER): Section ID
- `semester` (VARCHAR/STRING): Semester (Fall, Spring, Summer)
- `year` (INTEGER): Year
- `building` (VARCHAR/STRING): Building name (Foreign Key to classroom.building, part of composite key)
- `room_number` (INTEGER): Room number (Foreign Key to classroom.room_number, part of composite key)
- `time_slot_id` (VARCHAR/STRING): Time slot identifier (Foreign Key to time_slot.time_slot_id)

**Total Records**: 16 section offerings

**Complete Data**:
```
course_id: BIO-101, sec_id: 1, semester: Summer, year: 2017, building: Painter, room_number: 514, time_slot_id: B
course_id: BIO-301, sec_id: 1, semester: Summer, year: 2018, building: Painter, room_number: 514, time_slot_id: A
course_id: CS-101, sec_id: 1, semester: Fall, year: 2017, building: Packard, room_number: 101, time_slot_id: H
course_id: CS-101, sec_id: 1, semester: Spring, year: 2018, building: Packard, room_number: 101, time_slot_id: F
course_id: CS-190, sec_id: 1, semester: Spring, year: 2017, building: Taylor, room_number: 3128, time_slot_id: E
course_id: CS-190, sec_id: 2, semester: Spring, year: 2017, building: Taylor, room_number: 3128, time_slot_id: A
course_id: CS-315, sec_id: 1, semester: Spring, year: 2018, building: Watson, room_number: 120, time_slot_id: D
course_id: CS-319, sec_id: 1, semester: Spring, year: 2018, building: Watson, room_number: 100, time_slot_id: B
course_id: CS-319, sec_id: 2, semester: Spring, year: 2018, building: Taylor, room_number: 3128, time_slot_id: C
course_id: CS-347, sec_id: 1, semester: Fall, year: 2017, building: Taylor, room_number: 3128, time_slot_id: A
course_id: EE-181, sec_id: 1, semester: Spring, year: 2017, building: Taylor, room_number: 3128, time_slot_id: C
course_id: FIN-201, sec_id: 1, semester: Spring, year: 2018, building: Packard, room_number: 101, time_slot_id: B
course_id: HIS-351, sec_id: 1, semester: Spring, year: 2018, building: Painter, room_number: 514, time_slot_id: C
course_id: MU-199, sec_id: 1, semester: Spring, year: 2018, building: Packard, room_number: 101, time_slot_id: D
course_id: PHY-101, sec_id: 1, semester: Fall, year: 2017, building: Watson, room_number: 100, time_slot_id: A
```

**Building Distribution**: Packard (4 sections), Painter (3), Taylor (6), Watson (3)

**Room Distribution**: 
- Packard 101 (4 sections)
- Painter 514 (3 sections)
- Taylor 3128 (6 sections)
- Watson 100 (2 sections)
- Watson 120 (1 section)

**Time Slot Distribution**: A (4), B (3), C (4), D (3), E (1), F (1), H (1)

**Semester/Year Distribution**: Fall 2017 (3), Spring 2017 (4), Spring 2018 (8), Summer 2017 (1), Summer 2018 (1)

**Multiple Sections**: CS-190 has 2 sections in Spring 2017, CS-319 has 2 sections in Spring 2018

**Relationships**:
- Foreign key to `course` table via `course_id`
- Foreign key to `classroom` table via (`building`, `room_number`)
- Foreign key to `time_slot` table via `time_slot_id`
- Related to `takes` table via (`course_id`, `sec_id`, `semester`, `year`)
- Related to `teaches` table via (`course_id`, `sec_id`, `semester`, `year`)

---

## 8. udb_teaches.txt → teaches Table

**Columns**:
- `ID` (VARCHAR/STRING): Instructor ID (Foreign Key to instructor.ID)
- `course_id` (VARCHAR/STRING): Course ID (Foreign Key to course.course_id)
- `sec_id` (INTEGER): Section ID
- `semester` (VARCHAR/STRING): Semester (Fall, Spring, Summer)
- `year` (INTEGER): Year

**Total Records**: 16 teaching assignments

**Complete Data**:
```
ID: 10101, course_id: CS-101, sec_id: 1, semester: Fall, year: 2017
ID: 10101, course_id: CS-315, sec_id: 1, semester: Spring, year: 2018
ID: 10101, course_id: CS-347, sec_id: 1, semester: Fall, year: 2017
ID: 12121, course_id: FIN-201, sec_id: 1, semester: Spring, year: 2018
ID: 15151, course_id: MU-199, sec_id: 1, semester: Spring, year: 2018
ID: 22222, course_id: PHY-101, sec_id: 1, semester: Fall, year: 2017
ID: 32343, course_id: HIS-351, sec_id: 1, semester: Spring, year: 2018
ID: 45565, course_id: CS-101, sec_id: 1, semester: Spring, year: 2018
ID: 45565, course_id: CS-319, sec_id: 1, semester: Spring, year: 2018
ID: 76766, course_id: BIO-101, sec_id: 1, semester: Summer, year: 2017
ID: 76766, course_id: BIO-301, sec_id: 1, semester: Summer, year: 2018
ID: 83821, course_id: CS-190, sec_id: 1, semester: Spring, year: 2017
ID: 83821, course_id: CS-190, sec_id: 2, semester: Spring, year: 2017
ID: 83821, course_id: CS-319, sec_id: 2, semester: Spring, year: 2018
ID: 98345, course_id: EE-181, sec_id: 1, semester: Spring, year: 2017
```

**Instructor Teaching Distribution**:
- Instructor 10101 (Srinivasan) teaches: 3 sections
- Instructor 83821 (Brandt) teaches: 3 sections
- Instructor 76766 (Crick) teaches: 2 sections
- Instructor 45565 (Katz) teaches: 2 sections
- Other instructors teach: 1 section each

**Relationships**:
- Foreign key to `instructor` table via `ID`
- Foreign key to `section` table via (`course_id`, `sec_id`, `semester`, `year`)

---

## 9. udb_department.txt → department Table

**Columns**:
- `dept_name` (VARCHAR/STRING): Department name (Primary Key)
- `building` (VARCHAR/STRING): Building where department is located
- `budget` (INTEGER): Department budget

**Total Records**: 7 departments

**Complete Data**:
```
dept_name: Biology, building: Watson, budget: 90000
dept_name: Comp. Sci., building: Taylor, budget: 100000
dept_name: Elec. Eng., building: Taylor, budget: 85000
dept_name: Finance, building: Painter, budget: 120000
dept_name: History, building: Painter, budget: 50000
dept_name: Music, building: Packard, budget: 80000
dept_name: Physics, building: Watson, budget: 70000
```

**Budget Range**: $50,000 - $120,000

**Building Distribution**: Painter (2 departments), Taylor (2), Watson (2), Packard (1)

**Relationships**:
- Related to `student` table via `dept_name` (one department has many students)
- Related to `instructor` table via `dept_name` (one department has many instructors)
- Related to `course` table via `dept_name` (one department offers many courses)

---

## 10. udb_classroom.txt → classroom Table

**Columns**:
- `building` (VARCHAR/STRING): Building name (Part of Composite Primary Key)
- `room_number` (INTEGER): Room number (Part of Composite Primary Key)
- `capacity` (INTEGER): Maximum seating capacity

**Total Records**: 5 classrooms

**Complete Data**:
```
building: Packard, room_number: 101, capacity: 500
building: Painter, room_number: 514, capacity: 10
building: Taylor, room_number: 3128, capacity: 70
building: Watson, room_number: 100, capacity: 30
building: Watson, room_number: 120, capacity: 50
```

**Capacity Range**: 10 - 500 seats

**Building Distribution**: Packard (1 room), Painter (1), Taylor (1), Watson (2 rooms)

**Relationships**:
- Related to `section` table via (`building`, `room_number`) (one classroom can host many sections)

---

## 11. udb_timeslot.txt → time_slot Table

**Columns**:
- `time_slot_id` (VARCHAR/STRING): Time slot identifier (Part of Composite Primary Key)
- `day` (VARCHAR/STRING): Day of week (Part of Composite Primary Key) (M=Monday, T=Tuesday, W=Wednesday, R=Thursday, F=Friday)
- `start_hr` (INTEGER): Starting hour (24-hour format)
- `start_min` (INTEGER): Starting minute
- `end_hr` (INTEGER): Ending hour (24-hour format)
- `end_min` (INTEGER): Ending minute

**Total Records**: 21 time slot entries

**Complete Data**:
```
time_slot_id: A, day: M, start_hr: 8, start_min: 0, end_hr: 8, end_min: 50
time_slot_id: A, day: W, start_hr: 8, start_min: 0, end_hr: 8, end_min: 50
time_slot_id: A, day: F, start_hr: 8, start_min: 0, end_hr: 8, end_min: 50
time_slot_id: B, day: M, start_hr: 9, start_min: 0, end_hr: 9, end_min: 50
time_slot_id: B, day: W, start_hr: 9, start_min: 0, end_hr: 9, end_min: 50
time_slot_id: B, day: F, start_hr: 9, start_min: 0, end_hr: 9, end_min: 50
time_slot_id: C, day: M, start_hr: 11, start_min: 0, end_hr: 11, end_min: 50
time_slot_id: C, day: W, start_hr: 11, start_min: 0, end_hr: 11, end_min: 50
time_slot_id: C, day: F, start_hr: 11, start_min: 0, end_hr: 11, end_min: 50
time_slot_id: D, day: M, start_hr: 13, start_min: 0, end_hr: 13, end_min: 50
time_slot_id: D, day: W, start_hr: 13, start_min: 0, end_hr: 13, end_min: 50
time_slot_id: D, day: F, start_hr: 13, start_min: 0, end_hr: 13, end_min: 50
time_slot_id: E, day: T, start_hr: 10, start_min: 30, end_hr: 11, end_min: 45
time_slot_id: E, day: R, start_hr: 10, start_min: 30, end_hr: 11, end_min: 45
time_slot_id: F, day: T, start_hr: 14, start_min: 30, end_hr: 15, end_min: 45
time_slot_id: F, day: R, start_hr: 14, start_min: 30, end_hr: 15, end_min: 45
time_slot_id: G, day: M, start_hr: 16, start_min: 0, end_hr: 16, end_min: 50
time_slot_id: G, day: W, start_hr: 16, start_min: 0, end_hr: 16, end_min: 50
time_slot_id: G, day: F, start_hr: 16, start_min: 0, end_hr: 16, end_min: 50
time_slot_id: H, day: W, start_hr: 10, start_min: 0, end_hr: 12, end_min: 30
```

**Time Slot IDs**: A, B, C, D, E, F, G, H (8 unique time slot IDs)

**Time Slot Patterns**:
- Time slots A, B, C, D, G: Monday, Wednesday, Friday (MWF pattern)
- Time slot E, F: Tuesday, Thursday (TR pattern)
- Time slot H: Wednesday only (single day)

**Relationships**:
- Related to `section` table via `time_slot_id` (one time slot can be used by many sections)

---

## Summary Statistics

### Table Record Counts:
- **student**: 13 records
- **instructor**: 13 records
- **course**: 13 records
- **takes**: 22 records
- **prereq**: 7 records
- **advisor**: 9 records
- **section**: 16 records
- **teaches**: 16 records
- **department**: 7 records
- **classroom**: 5 records
- **time_slot**: 21 records

### Departments (7 total):
1. Biology
2. Comp. Sci.
3. Elec. Eng.
4. Finance
5. History
6. Music
7. Physics

### Buildings (4 total):
1. Packard
2. Painter
3. Taylor
4. Watson

### Semesters Represented:
- Fall 2017
- Spring 2017
- Spring 2018
- Summer 2017
- Summer 2018

### Grade Values:
A, A-, B+, B, B-, C+, C, C-, D+ (implied), D (implied), D- (implied), F, F+ (implied), null

---

## Entity Relationship Summary

### Core Entities:
1. **student** - Enrolled students (13 records)
2. **instructor** - Faculty members (13 records)
3. **course** - Courses offered (13 records)
4. **department** - Academic departments (7 records)
5. **section** - Course sections/offerings (16 records)
6. **classroom** - Physical rooms (5 records)
7. **time_slot** - Scheduling time periods (21 records)

### Relationship Tables:
1. **takes** - Student enrollments (22 records) - Links student ↔ course section
2. **teaches** - Instructor assignments (16 records) - Links instructor ↔ course section
3. **advisor** - Academic advising (9 records) - Links student ↔ instructor
4. **prereq** - Course prerequisites (7 records) - Links course ↔ course (self-referential)

---

## Common Query Patterns

### Joins:
- **Student-Course Enrollment**: `student` JOIN `takes` JOIN `course`
- **Instructor-Course Teaching**: `instructor` JOIN `teaches` JOIN `section` JOIN `course`
- **Student-Advisor**: `student` LEFT OUTER JOIN `advisor` JOIN `instructor`
- **Course Prerequisites**: `course` JOIN `prereq` (self-join)
- **Section Details**: `section` JOIN `classroom` JOIN `time_slot`

### Common WHERE Conditions:
- Filter by department: `dept_name = 'Comp. Sci.'`
- Filter by grade: `grade = 'A'` or `grade = 'F'`
- Filter by semester/year: `semester = 'Fall' AND year = 2017`
- Filter by student: `ID = '12345'`
- Filter by course: `course_id = 'CS-101'`
- Filter by building: `building = 'Taylor'`

### Common Aggregations:
- Count students: `COUNT(*)` on `student` table
- Count courses: `COUNT(*)` on `course` table
- Count grades: `COUNT(grade)` with `WHERE grade = 'A'`
- Average salary: `AVG(salary)` on `instructor` table
- Sum budget: `SUM(budget)` on `department` table

---

## Important Notes

1. **Primary Keys**: Most tables use single-column primary keys (ID, course_id, dept_name, time_slot_id), while some use composite keys (section, takes, teaches, advisor, classroom, time_slot).

2. **Foreign Keys**: While foreign key relationships exist logically, some foreign key constraints may not be enforced in the database.

3. **NULL Values**: The `grade` column in `takes` can be NULL (indicating a course in progress or no grade assigned yet).

4. **Grade System**: Letter grades include: A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F+, F. NULL is also possible.

5. **Semester Values**: Semesters are stored as strings: 'Fall', 'Spring', 'Summer'.

6. **Department Names**: Some department names include periods (e.g., 'Comp. Sci.', 'Elec. Eng.').

7. **Time Slot Structure**: Time slots can span multiple days (e.g., time slot A is Monday, Wednesday, Friday at the same time).

8. **Multiple Sections**: Some courses have multiple sections in the same semester (e.g., CS-190 has sections 1 and 2 in Spring 2017).

9. **Missing Advisors**: 4 students (19991, 54321, 55739, 70557) do not have advisors listed in the advisor table.

10. **Self-Referential Relationships**: The `prereq` table creates a self-referential relationship on the `course` table.

---

This document provides a complete reference for understanding the University Database structure, relationships, and data patterns based on the provided udb_*.txt files.
