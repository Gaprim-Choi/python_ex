#리스트 내포
number = [1,2,3,4,5]

square = []

for i in number:
    if i >=3:
        square.append(i**2)
print(square)

number = [1,2,3,4,5]

square = [i**2 for i in number if i>=3]
print(square)