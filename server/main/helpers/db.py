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
