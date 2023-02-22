from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools


student_roster_iterator = iter(student_roster)
for student in range(len(student_roster)):
  print(next(student_roster_iterator))

organizer = ClassroomOrganizer()

for student in organizer:
  print(student)

combinations = organizer.combinations()
print(combinations)

afterschoolprogram = organizer.get_students_with_subject("Math")
afterschoolprogram += organizer.get_students_with_subject("Science")

afterschoolprogram_list = list(itertools.combinations(afterschoolprogram, 4))
print("--- List of After School Program ---")
print(afterschoolprogram_list)