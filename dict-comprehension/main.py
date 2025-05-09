import random

# dictionary coprehension
# new_dict = {new_key: new_value for item in list}

student_names = ["bob", 'adam', 'casey', 'john', 'alex', 'jax']

student_scores = {student: random.randint(1, 100)  for student in student_names}
print(f"scores: {student_scores}")

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(f"result: {passed_students}")