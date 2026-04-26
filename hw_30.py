import json
from datetime import datetime
from collections import defaultdict

def analyze_students(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            students = json.load(file)
            total_students = len(students)
            total_age = 0
            course_count = defaultdict(int)
        for student in students:
            birth = datetime.strptime(student["birth_date"], "%d.%m.%Y")
            enroll = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

            #total_age += enroll.toordinal() - birth.toordinal()
            total_age += enroll.year - birth.year - ((enroll.month, enroll.day) < (birth.month, birth.day))

            for course in student["courses"]:
                course_count[course] += 1
        #average_age = round((total_age / total_students) / 365.2425, 1)
        average_age = round(total_age / total_students, 1)

        result = {
            "total_students": total_students,
            "average_enrollment_age": average_age,
            "students_per_course": dict(course_count)
        }
        return result
    except json.JSONDecodeError as e:
        return (f"Ошибка декодирования JSON: {e}")


def save_report(data, filename="student_courses_report.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, sort_keys=True, ensure_ascii=False)


# result = analyze_students("student_courses.json")
# print(result)
save_report(analyze_students("student_courses.json"))
