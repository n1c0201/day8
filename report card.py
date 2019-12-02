eren = {
    "name": "Eren",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
        }
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
        }

armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
         }

student = (eren, mikasa, armin)
for i in student:
    for j in i:
        print(j, ": ", i[j])
    print("")

def average(numbers: list):
    total = float(sum(numbers) / len(numbers))
    return total

def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6

    return homework + quizzes + tests

def get_letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"
score = get_letter_grade(get_average(eren))
print(score)

def get_class_average(stud: list):
    results = []
    for i in stud:
        score = get_average(i)
        results.append(score)
    return average(results)

students = [eren, mikasa, armin]
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))

