a=0
print(a)

a=a+1
print(a)

a=a+1
print(a)

a=a+1
print(a)

a=a+1
print(a)

a=a+1
print(a)

'''
0
1
2
3
4
5
'''

# for 문의 구조
# for<반복 변수>in<반복 범위>
#    <코드 블록>
for a in [0,1,2,3,4,5]:
    print(a)

'''
0
1
2
3
4
5
'''

myFriends =['James','Robetr','Lisa','Mary']

for myFriends in myFriends:
    print(myFriends)


'''
James
Robetr
Lisa
Mary
'''

print(range(0,10,1))
print(list(range(0,10,1)))

for a in range(0,10,1):
    print(a)
'''
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0
1
2
3
4
5
6
7
8
9
'''


print(list(range(0,10,1)))
print(list(range(0,10)))
print(list(range(10)))

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print(list(range(0,20,5)))
print(list(range(-10,0,2)))
print(list(range(3,-10,-3)))
print(list(range(0,-5,1)))

'''
[0, 5, 10, 15]
[-10, -8, -6, -4, -2]
[3, 0, -3, -6, -9]
[]
'''

x_list=['x1','x2']
y_list=['y1','y2']

print("x y")
for x in x_list:
    for y in y_list:
        print(x,y)

'''
x y
x1 y1
x1 y2
x2 y1
x2 y2
'''


names = ['James','Robetr','Lisa','Mary']
scores = [95, 96, 97, 94]

for k in range(len(names)):
    print(names[k],scores[k])

'''
James 95
Robetr 96
Lisa 97
Mary 94
'''

for name,score in zip(names,scores):
    print(name,score)

'''
James 95
Robetr 96
Lisa 97
Mary 94
'''