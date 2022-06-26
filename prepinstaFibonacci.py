firstNum = 0
secondNum = 1
ip = input("enter the 'n'th term: ")
print("The fibonacci series is 0 1 ", end="")
for i in range(int(ip) - 2):
    thirdNum = firstNum + secondNum
    secondNum = thirdNum
    firstNum = secondNum
    print(thirdNum, end=" ")
