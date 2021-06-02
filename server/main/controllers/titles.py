from ..helpers import db
from ..models.title import Title


class Titles:
    @staticmethod
    def add_title(data: dict):
        """
        Add title into database
        """
        titles = Title(data.title_name)
        db.Database.add("titles", titles.db_data())

    @staticmethod
    def delete_title(current_id: int):
        """
        Delete title from database
        """
        db.Database.delete("titles", current_id)

    @staticmethod
    def show_all_titles():
        """
        Show all title from database
        """
        return db.Database.show_table('titles')