import components.teachers.service as teacher_service
import pprint

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

pprint.pprint(teacher_service.get_all())

pprint.pprint("--------------------------------------")


pprint.pprint(teacher_service.delete_one_by_id(3))

pprint.pprint("--------------------------------------")

pprint.pprint(teacher_service.get_all())

# print(teacher.get_one_by_id(1))

# print(teacher.update_one_by_id(4, {
#       "name": "Не Смирнова Екатерина",
#       "contacts": {
#           "email": "нет@example.com",
#           "phone": "+1122334455"
#       }}))
