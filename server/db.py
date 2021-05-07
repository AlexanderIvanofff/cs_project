from string import Template

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BlaBla123",
    database="computer_science",
)


class Database:
    @staticmethod
    def add(table, key_value):
        my_cursor = mydb.cursor()
        keys = ''
        values = ''
        for key, value in key_value.items():
            keys += "`" + key + "`,"
            values += "'" + value + "',"
        keys = keys[:-1]
        values = values[:-1]

        sql_two = Template(
            "INSERT INTO `computer_science`.`$table` ( $keys ) VALUES ( $values );")

        my_cursor.execute(sql_two.safe_substitute(table=table, keys=keys, values=values))
        mydb.commit()

    @staticmethod
    def delete(table, current_id):
        my_cursor = mydb.cursor()

        sql_two = Template(
            "DELETE FROM `computer_science`.`$table` WHERE id = '$id';")
        my_cursor.execute(sql_two.safe_substitute(table=table, id=current_id))
        mydb.commit()

    @staticmethod
    def edit(table, key_name, key_value, update_id):
        my_cursor = mydb.cursor()

        sql_two = Template(
            "UPDATE `computer_science`.`$table` SET `$key_name` = '$key_value' WHERE (`id` = '$current_id');")
        my_cursor.execute(
            sql_two.safe_substitute(table=table, key_name=key_name, key_value=key_value, current_id=update_id))
        mydb.commit()

    @staticmethod
    def show_table(table):
        my_cursor = mydb.cursor()

        sql_two = Template(
            "SELECT * FROM (`computer_science`.$table)"
        )

        my_cursor.execute(
            sql_two.safe_substitute(table=table)
        )

        return my_cursor.fetchall()

    @staticmethod
    def show_top_three_courses(table):
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
    def show_all_students_and_there_courses(table):
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
    def show_all_professors_courses_and_students_count(table):
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
    def show_top_three_professors_enrolled_students_in_courses(table):
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