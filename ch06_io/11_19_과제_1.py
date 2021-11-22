#input1 = int(input("첫번째 숫자를 입력하세요: "))
#input2 = int(input("두번째 숫자를 입력하세요: "))
#total = input1 + input2
#print("두 수의 합은 %s 입니다." %total)

#f1 = open("./ch06_io/test.txt", 'w')
#f1.write('Life is too short\nyou need java')
#f1.close()
#f2 = open("./ch06_io/test.txt", 'r')
#print(f2.readline())
#f2.close()

#user_input = input("저장할 내용을 입력하세요: ")
#f = open("./ch06_io/test.txt", 'a')
#f.write("\n") ## 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
#f.write(user_input)
#f.close()

#f = open('./ch06_io/test.txt', 'r')
#body = f.read() # test.txt 파일의 내용을 body 변수에 저장
#f.close()
#body = body.replace('java','python') # body 문자열에서 'java'를 'python'으로 변경
#f = open('./ch06_io/test.txt', 'w') # 파일을 쓰기 모드로 다시 실행
#f.write(body)
#f.close()

#f = open("./ch06_io/sample.txt", 'r')
#lines = f.read().splitlines() # sample.txt를 줄 단위로 모두 읽는다.
#print(lines)
#f.close()
#total = 0
#for line in lines:
# score = int(line)# 줄에 적힌 점수를 숫자형으로 변환한다.
# total += score
#average = total/len(lines)
#f = open("./ch06_io/result.txt",'w')
#f.write(str(average))
#f.close()