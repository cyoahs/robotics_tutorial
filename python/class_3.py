class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    def learn(self):
        print('Learn something')
    
    def print_score(self):
        print(f"{self.name}'s score is {self.__score}")

class MechanicsStudent(Student):
    def learn(self):
        print('Learn mechanics')

class PhysicsStudent(Student):
    def learn(self):
        print('Learn physics')
    
    def play(self, game):
        print(f'Play {game}')

xiao_ming = Student('Xiao Ming', 99)
xiao_qiang = MechanicsStudent('Xiao Qiang', 100)
xiao_huang = PhysicsStudent('Xiao Huang', 70)

xiao_qiang.print_score()
xiao_huang.print_score()
xiao_ming.learn()
xiao_qiang.learn()
xiao_huang.learn()
xiao_huang.play('Warcraft III')

