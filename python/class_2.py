class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    def get_score(self):
        return self.__score
    
    def print_score(self):
        print(f"{self.name}'s score is {self.__score}")

xiao_ming = Student('Xiao Ming', 99)
print(xiao_ming.name)
xiao_ming.print_score()

print(xiao_ming.__score)
print(xiao_ming.get_score())

