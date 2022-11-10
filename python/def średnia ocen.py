

#uwaga jeśli jako domyślny argument chcemy użyć listy lub słownika !!!!

#wylicz średnią ocen końcowych
def write_final_grade(subject_grades,final_grades=None):
    if final_grades is None:
        #do listy naszych przedmiotów ma dołożyć kolejną ocenę końcową
        final_grades = []
    grades_avg = sum(subject_grades) / len(subject_grades)
    final_grades.append(int(grades_avg))
    return final_grades

john_math_grades = [3, 5, 2, 6]
john_physic_grades = [4, 6, 3, 5]
john_final_grades = write_final_grade(subject_grades=john_math_grades)
john_final_grades = write_final_grade(subject_grades=john_physic_grades,final_grades=john_final_grades)
print(f"Oceny końcowe John'a: {john_final_grades}")
#to samo można zrobić dla bob'a