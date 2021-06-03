from ..helpers import db
from ..models.professor import Professor


class Professors:
    @staticmethod
    def add_professors(data: dict):
        """
        Add professor into database
        """
        professor = Professor(data["first_name"], data["last_name"])
        db.Database.add('professors', professor.db_data())

    @staticmethod
    def delete_professors(current_id: int):
        """
        Delete professor into database
        """
        db.Database.delete("professors", current_id)

    @staticmethod
    def show_all_professors():
        """
        Show all professor into database
        """
        return db.Database.show_table('professors')
