from main.helpers.db import mydb
from string import Template


class StatsModel:
    @staticmethod
    def get_top_courses(table):
        my_cursor = mydb.cursor()
        sql_two = Template(
            "SELECT courses.title, count(students.course_id) AS number_f_courses "
            "FROM (courses INNER JOIN students ON students.course_id=courses.id) "
            "GROUP BY title "
            "LIMIT 3")
        my_cursor.execute(
            sql_two.safe_substitute(table=table)
        )
        return my_cursor.fetchall()

    @staticmethod
    def get_all_students_and_there_courses(table):
        my_cursor = mydb.cursor()
        sql_two = Template(
            "SELECT students.*, courses.* "
            "FROM (courses JOIN students ON students.course_id=courses.id)"
            "order by students.first_name ASC")
        my_cursor.execute(
            sql_two.safe_substitute(table=table)
        )
        return my_cursor.fetchall()

    @staticmethod
    def get_all_professors_courses_and_students_count(table):
        my_cursor = mydb.cursor()
        sql_two = Template(
            "SELECT professors.*, courses.*, students.*, COUNT(*) "
            "FROM professors, courses, students  "
            "WHERE courses.professor_id=professors.id and students.course_id=courses.id "
            "GROUP BY title")
        my_cursor.execute(
            sql_two.safe_substitute(table=table)
        )
        return my_cursor.fetchall()

    @staticmethod
    def get_top_professors_enrolled_students_in_courses(table):
        my_cursor = mydb.cursor()
        sql_two = Template(
            "SELECT students.first_name, courses.title, professors.*, count(students.course_id) AS number_f_courses "
            "FROM (courses INNER JOIN students ON students.course_id=courses.id "
            "INNER JOIN professors ON professors.id=courses.professor_id) "
            "GROUP BY title "
            "LIMIT 3")
        my_cursor.execute(
            sql_two.safe_substitute(table=table)
        )
        return my_cursor.fetchall()
