list = [1,2,3,4] # list: [1, 2, 3, 4]
print('list:',list)
list.append(5) # append: [1, 2, 3, 4, 5]
print('append:',list)

temp ='123'
list.extend(temp)
print('extend:',list) # extend: [1, 2, 3, 4, 5, '1', '2', '3']

list.remove(1)
print('remove:',list) # remove: [2, 3, 4, 5, '1', '2', '3']

list.pop(-1)
print('pop:',list) # pop: [2, 3, 4, 5, '1', '2']

list.clear()
print('clear:',list) # clear: []

list=['a','b','c','d','e']

print('index:',list.index('c')) # index: 2

print('count:',list.count('a')) # count: 1
list=[7,5,4,3,2,7,1,2,3]
list.sort()
print('sort:',list) # sort: [1, 2, 2, 3, 3, 4, 5, 7, 7]

list.reverse()
print('reverse:',list) # reverse: [7, 7, 5, 4, 3, 3, 2, 2, 1]

copy_list=list.copy()
print('copy:',copy_list) # copy: [7, 7, 5, 4, 3, 3, 2, 2, 1]