# 这个符号代表注释
# 在print中使用逗号时，会在同一行隔开一个空格输出
# 对字符串使用加法，会自动拼接字符串
a = 'str'
b = 'ing'
c = a + b
print(c)
print(a, b)

c = 233
print(a, c)

# format格式化
d = '{} is {}'.format(a, c)
print(d)
print('{} is {}'.format(a, c))
print('保留两位小数 {:.2f}'.format(c))
print('按照c a c的顺序输出\n{1} {0} {1}'.format(a, c))

# f-string格式化
d = f'这是更简单的方法：{a} {c} {c/10} {1+2}'
print(d)

