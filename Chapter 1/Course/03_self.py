class Student:
    name = None
    age = None

    def hello(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans")

    def say_hi(self, msg):
        print(f"Bonjour à tous, {msg}")

# Création d'un objet
stu = Student()
stu.name = "Alex"
stu.age = 18
stu.hello()
stu.say_hi("enchanté.")