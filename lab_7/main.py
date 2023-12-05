import components.teachers.service as teacher


# print(teacher.create_one({
#       "name": "Тест Тест",
#       "courses_id": [
#           1,
#           2
#       ],
#       "contacts": {
#           "email": "тест@example.com",
#           "phone": "+333333"
#       }}))


print(teacher.delete_one_by_id(4))

# print(teacher.get_all())

# print(teacher.get_one_by_id(1))

# print(teacher.update_one_by_id(4, {
#       "name": "Не Смирнова Екатерина",
#       "contacts": {
#           "email": "нет@example.com",
#           "phone": "+1122334455"
#       }}))
