def getInput():
    with open("input.txt") as f:
        list1 = []
        list2 = []
        input = f.read()

    for line in input.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    return list1, list2

print(getInput())