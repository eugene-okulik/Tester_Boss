text1 = "результат операции: 42"
num1 = int(text1[text1.index(':') + 1:].strip())
print(num1 + 10)

text2 = "результат операции: 514"
num2 = int(text2[text2.index(':') + 1:].strip())
print(num2 + 10)

text3 = "результат работы программы: 9"
num3 = int(text3[text3.index(':') + 1:].strip())
print(num3 + 10)
