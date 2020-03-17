def my_function(a):
    return a + a

print(my_function(100))
print(my_function('Hello'))

def my_second_function(a, c):
    b = a + c
    return a, b

c, d = my_second_function(1, 3)
print(c, d)

def my_third_function(name, age, major='unknown', language='python'):
    print(f"{name}'s age is {age}")
    print(f"{name}'s major is {major}")
    print(f'{name} codes in {language}')
    print('------------------------------')

my_third_function('Adam', 18)
my_third_function('Adam', 18, 'Mechanics')
my_third_function('Adam', 18, language='C++')
my_third_function(name='Adam', age=18, language='Rust', major='CS')

my_fourth_function = lambda x: x*x
print(my_fourth_function(11))

