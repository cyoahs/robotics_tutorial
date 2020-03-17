# range
for i in range(10):
    print(i, end=' ') # 取消换行

for i in range(5, 10):
    print(i, end=' ')

for i in range(5, 10, 2):
    print(i, end=' ')

# loop over a list
courses = ['Calculus', 'Linear Algebra', 'Mechanics']
# low-level
for i in range(3):
    print(courses[i])
# advanced
for course in courses:
    print(course)
# advanced
for i, course in enumerate(courses):
    print(f'The No.{i+1} course is {course}')

# list a range
mylist = list(range(1, 101))
print(mylist)
sum = 0
for i in mylist:
    sum += i
print(sum)

