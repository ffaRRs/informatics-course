from db import db


def get_one_by_id(id):

    for elem in db["teachers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():

    return db["teachers"]


def update_one_by_id(id, teacher):

    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            elem["name"] = teacher["name"]
            elem["contacts"] = teacher["contacts"]

            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            candidate = db["teachers"].pop(i)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(teacher):

    last_teacher_id = get_all()[-1]["id"]
    db["teachers"].append({"id": last_teacher_id + 1, **teacher})
