from ..helpers import db


class ProfessorModel:
    @staticmethod
    def add(data):
        """
        Add professor into database
        """
        professor = Professor(data['first_name'], data["last_name"])
        return db.Database.add('professors', professor.db_data())

    @staticmethod
    def delete(current_id):
        """
        Delete professor into database
        """
        db.Database.delete("professors", current_id)

    @staticmethod
    def show_all_professors():
        """
        Show all title into database
        """
        return db.Database.show_table("professors")


class Professor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def db_data(self):
        return {"first_name": self.first_name, "last_name": self.last_name}
