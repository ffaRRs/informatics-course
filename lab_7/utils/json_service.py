import json


def get_database():
    with open("db.json", encoding="utf-8") as db_file:
        return json.load(db_file)


def set_database(db):
    with open("db.json", "w", encoding="utf-8", ) as db_file:
        json.dump(db, db_file, ensure_ascii=False)
