from ..helpers import db


class TitleModel:
    @staticmethod
    def add(data):
        """
        Add title into database
        """
        title = Title(data["title_name"])
        return db.Database.add("titles", title.db_data())

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


class Title:
    def __init__(self, title_name):
        self.title_name = title_name

    def db_data(self):
        return {"title_name": self.title_name}
