import statistics

default_surname = 'Петров'
default_name = 'Петр'
default_patronymic = 'Петрович'
default_year = 2000
default_course = 1
default_group = '100'
default_grades = [2, 2, 2, 2, 2]

max_grade = 5
min_grade = 2
count_grade = 5

first_course = 1
sixth_course = 6

min_year = 1900
max_year = 2023

class Student:
    def __init__(self, surname=default_surname, name=default_name, patronymic=default_patronymic, year=default_year,
                 course=default_course, group=default_group, grades=default_grades):
        self.Group = group

        if(not (surname.isalpha() and name.isalpha() and patronymic.isalpha())):
            self.Surname = default_surname
            self.Name = default_name
            self.Patronymic = default_patronymic
        else:
            self.Surname = surname
            self.Name = name
            self.Patronymic = patronymic

        if(not surname.istitle()):
            self.Surname = self.Surname.title()

        if (not name.istitle()):
            self.Name = self.Name.title()

        if (not patronymic.istitle()):
            self.Patronymic = self.Patronymic.title()

        if (year < min_year or year > max_year or type(year) is not int):
            self.Year = default_year
        else:
            self.Year = year

        if (course < first_course or course > sixth_course or type(course) is not int):
            self.Course = default_course
        else:
            self.Course = course

        if (len(grades) != count_grade):
            self.Grades = default_grades
        else:
            for grade in grades:
                if grade < min_grade or grade > max_grade or type(grade) is not int:
                    self.Grades = default_grades
                    return
            self.Grades = grades

def print_students(students):
    sorting_students_by_surname = sorted(students, key=lambda student: student.Surname)
    return sorted(sorting_students_by_surname, key=lambda student: student.Course)

def find_mean(students):
    groups = {student.Group for student in students}
    average_result = {}

    for group in groups:
        mean_grades = []

        for subject in range(count_grade):
            subject_grade = [student.Grades[subject]
                             for student in students
                             if student.Group == group]
            mean_grade = statistics.mean(subject_grade)
            mean_grades.append(mean_grade)

        average_result[group] = mean_grades

    return average_result

def find_younger_and_older_students(students):
    younger_student = max(students, key=lambda student: student.Year)
    younger_students = [student for student in students if student.Year == younger_student.Year]

    older_student = min(students, key=lambda student: student.Year)
    older_students = [student for student in students if student.Year == older_student.Year]

    return younger_students, older_students

def get_best_students (students):
    groups = {student.Group for student in students}
    best_students = {}

    for group in groups:
        best_student = max(students, key=lambda student: statistics.mean(student.Grades) if student.Group == group else 0)
        best_students_in_group = [student for student in students if statistics.mean(student.Grades) == statistics.mean(best_student.Grades)]
        for student in best_students_in_group:
            best_students[group] = student

    return best_students

if __name__ == '__main__':
    students = [
        Student('Петров', 'Антон', 'Петрович', 2000, 4, '108', [5, 4, 5, 5, 5]),
        Student('Матюхин', 'Владимир', 'Сергеевич', 2002, 2, '100', [4, 4, 3, 4, 5]),
        Student('Смирнова', 'Екатерина', 'Семеновна', 2001, 3, '109', [5, 5, 5, 3, 5]),
        Student('Тихонов', 'Константин', 'Владимирович', 1999, 4, '108', [4, 4, 4, 4, 4]),
        Student('Талалаева', 'Ксения', 'Анатольевна', 2002, 3, '109', [5, 4, 3, 4, 4]),
        Student('Бабурин', 'Семен', 'Семенович', 2002, 2, '100', [2, 4, 4, 3, 4]),
        Student('Пятифанов', 'Роман', 'Петрович', 2000, 4, '108', [5, 4, 4, 4, 5]),
        Student('Морозова', 'Полина', 'Марковна', 2001, 3, '109', [5, 5, 5, 5, 5]),
        Student('Дронин', 'Михаил', 'Михайлович', 2002, 2, '100', [4, 3, 5, 4, 4])
    ]