a = "Life is too short, you need python."
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

i = 0
while True:
 i += 1
 if i>5:break
 print("*"*i )


A = [70,60,55,75,95,90,80,85,100]
total = 0
for i in A:
 total += i
average = round(total/len(A),2)
print(average)
