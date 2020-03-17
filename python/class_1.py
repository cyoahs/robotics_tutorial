class Student(object):
    def __init__(self, name, score_, age):
        self.name = name
        self.score = score_
        self.age = age
    
    def print_score(self):
        print(f"{self.name}'s score is {self.score}")
    
    def print_age(self):
        print(f"{self.name}'s age is {self.age}")

xiao_ming = Student('Xiao Ming', 99, 18)
print(xiao_ming.name)
print(xiao_ming.score)
xiao_ming.print_score()
xiao_ming.print_age()

