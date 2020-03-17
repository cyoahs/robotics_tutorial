list1 = [1, 2, 4, 3]
list2 = ['name', 'score', 100]
print(list1)
print(list1[0])
print(list1[1:3]) # 左闭右开区间
print(list1[:2]) # 相当于MATLAB的start:1
print(list1[1:]) # 相当于MATLAB的1:end
print(list1[-1])

list1.sort()
print(list1)

list2.insert(1, 'C++')
print(list2)
list2.remove('score')
print(list2)
idx = list2.index('name')
print(idx)
list2.pop(0)
print(list2)

list1.append(5)
print(list1)
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)

