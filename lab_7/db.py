db = {
    "school_name": "Школа №1",
    "address": "ул. Школьная, 123",
    "students": [
        {
            "id": 1,
            "name": "Иванов Иван",
            "age": 15,
            "contacts": {
                "email": "ivanov@example.com",
                "phone": "+1234567890"
            },
            "class_id": 1
        },
        {
            "id": 2,
            "name": "Петрова Анна",
            "age": 16,
            "contacts": {
                "email": "annapetrova@example.com",
                "phone": "+0987654321"
            },
            "class_id": 2
        },
        {
            "id": 3,
            "name": "Сидоров Петр",
            "age": 15,
            "contacts": {
                "email": "sidorov@example.com",
                "phone": "+5678901234"
            },
            "class_id": 1
        },
        {
            "id": 3,
            "name": "Сидоров Петр",
            "age": 15,
            "contacts": {
                "email": "sidorov@example.com",
                "phone": "+5678901234"
            },
            "class_id": 2
        }
    ],
    "classes": [
        {
            "id": 1,
            "grade": 9,
            "letter": "A",
            "class_teacher_id": 1,
            "students_id": [
                1,
                3
            ],
            "courses_id": [
                1,
                2,
                3
            ]
        },
        {
            "id": 2,
            "grade": 10,
            "letter": "A",
            "class_teacher_id": 2,
            "students_id": [
                2,
                4
            ],
            "courses_id": [
                1,
                3
            ]
        }
    ],
    "teachers": [
        {
            "id": 1,
            "name": "Смирнова Екатерина",
            "courses_id": [
                1,
                2
            ],
            "contacts": {
                "email": "smirnova@example.com",
                "phone": "+1122334455"
            }
        },
        {
            "id": 2,
            "name": "Иванова Ольга",
            "courses_id": [
                3
            ],
            "contacts": {
                "email": "ivanova@example.com",
                "phone": "+9988776655"
            }
        },
        {
            "id": 3,
            "name": "Петров Иван",
            "courses_id": [
                1
            ],
            "contacts": {
                "email": "petrov@example.com",
                "phone": "+3344556677"
            }
        }
    ],
    "courses": [
        {
            "id": 1,
            "name": "Физика",
            "teachers_id": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Математика",
            "teachers_id": [
                3
            ]
        },
        {
            "id": 3,
            "name": "Математика",
            "teachers_id": [
                1,
                2
            ]
        }
    ]
}
