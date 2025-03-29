class Student :
    name = None # Enregister le nom de l'élève

# Création d'objets basés sur des classes
stu_1 = Student()
stu_2 = Student()

# Affection des propriétés de l'objet
stu_1.name = "Alex"
stu_2.name = "Micha"
print(stu_1.name)
print(stu_2.name)