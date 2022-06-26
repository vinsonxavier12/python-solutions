low, high = map(int, input("Enter the low and high: ").split())
primeNumbers = []
for number in range(low, high):
    flag = 0
    for i in range(2, number):
        if number % i == 0:
            flag = 1
    if flag == 0:
        primeNumbers.append(number)
print(primeNumbers)
