import db


class Title:
    @staticmethod
    def add_title(key_value: dict):
        """
        Add title into database
        """
        db.Database.add("titles", key_value)

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


title = Title()