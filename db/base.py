import sqlite3
from pathlib import Path

class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).resolve().parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS films")
        self.db.commit()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS films (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                year INTEGER,
                description TEXT,
                picture TEXT
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO films (name, year, description, picture)  
            VALUES 
                ('Прочь', 2017, 'Знакомство с родителями подружки не предвещает молодому фотографу из Нью-Йорка ничего хорошего, ведь семья девушки принадлежит к элитному обществу и живет в уединенном загородном доме. Если бы он только знал истинную причину своего приглашения, то немедленно бросился бы прочь...', 'proch.jpeg'),
                ('Гарри Поттер', 2001, 'Жизнь десятилетнего Гарри Поттера нельзя назвать сладкой: его родители умерли, едва ему исполнился год, а от дяди и тётки, взявших сироту на воспитание, достаются лишь тычки да подзатыльники. Но в одиннадцатый день рождения Гарри всё меняется.', 'potter.jpeg'),
                ('Дюна: часть вторая', 2024, 'Герцог Пол Атрейдес присоединяется к фременам, чтобы стать Муад Дибом, одновременно пытаясь остановить наступление войны.', 'dune.jpeg')
            """
        )
        self.db.commit()

    def get_film_by_id(self, id: int):
        self.cursor.execute(
            "SELECT * FROM films WHERE id = :id",
            {"id": id},
        )
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database()
    # db.drop_tables()
    db.create_tables()
    #db.populate_tables()
