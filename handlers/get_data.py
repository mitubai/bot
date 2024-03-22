import sqlite3
from pathlib import Path

class Data:
    def __init__(self) -> None:
        db_path = Path(__file__).resolve().parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def get_data(self):
        self.cursor.execute("SELECT * FROM films")
        return self.cursor.fetchall()

    def get_proch(self):
        self.cursor.execute("SELECT * FROM films WHERE id = 1")
        return self.cursor.fetchone()

    def get_potter(self):
        self.cursor.execute("SELECT * FROM films WHERE id = 2")
        return self.cursor.fetchone()

    def get_dune(self):
        self.cursor.execute("SELECT * FROM films WHERE id = 3")
        return self.cursor.fetchone()


if __name__ == "__main__":
    get_data = Data()
    data = get_data.get_data()
    # print(get_data.get_film_by_id(1))
    # print(get_data.get_if_by_film("Прочь"))
    # print(get_data.get_proch(2017))
    print(get_data.get_proch())
    # print(get_data.get_one_dish(2))
    # for row in data:
    #print(row)