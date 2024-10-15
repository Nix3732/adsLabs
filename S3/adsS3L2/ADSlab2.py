from queue import LifoQueue, Queue
import sys

PRIORITY = {"(": 1, "+": 2, "-": 2, "*": 3, "/": 3}

def brakets(math):
    math = str(math)
    if math.find(')') < math.find('('):
        return -1
    while '(' in math:
        math = math.replace('(', '', 1)
        if ')' in math:
            math = math.replace(')', '', 1)
        else:
            return -2
    if '(' not in math and ')' not in math:
        return 1
    elif ')' in math:
        return -3

def data(math):
    n = list(math)
    m = []
    a = ''
    result = ''
    for i in n:
        if i not in operation and i not in '()':
            if i.isdigit():
                a = a + str(i)
            else:
                return -5
        elif i in operation or i in '()':
            m.append(a)
            a = ''
            m.append(i)

    if n[-1].isdigit():
        m.append(a)
    m = [x for x in m if x != '']

    if len(m) < 3:
        return -6

    digitCounter = 0
    operationBool = False

    for i in m:
        if i.isdigit():
            digitCounter += 1
        if i in '+-*/':
            operationBool = True
    if digitCounter < 2:
        return -7
    if not operationBool:
        return -8

    return m

def rpn(math):
    result = ''
    m = math
    for i in m:
        flag = 0
        if i.isdigit():
            result = result + i

        elif i in operation:
            if len(r) != 0:
                for j in r:
                    if PRIORITY.get(i) > PRIORITY.get(j):
                        flag += 1
                if flag == len(r):       
                    r.append(i)
                    flag = 0
                    continue
            else:
                r.append(i)
                continue
            flag = 0

            while True:
                if len(r) != 0 and PRIORITY.get(r[-1]) >= PRIORITY.get(i):
                    result = result + r[-1]
                    r.pop(-1)
                else:
                    break
                

            if len(r) != 0:
                for j in r:
                    if PRIORITY.get(i) > PRIORITY.get(j):
                        flag += 1
                if flag == len(r):       
                    r.append(i)
                    flag = 0
                    continue
            else:
                r.append(i)
                continue
            flag = 0
            
        elif i == '(':
            r.append(i)
        elif i == ')':
            while r[-1] != '(':
                result = result + r[-1]
                r.pop(-1)
            if r[-1] == '(':
                r.pop(-1)
       
    while len(r) != 0:
        result = result + r[-1]
        r.pop(-1)
    return result

def evaluate(math): 
    stack = LifoQueue()
    for sym in math:
        if sym not in operation:
            stack.put(float(sym))
        else:
            a = stack.get()
            b = stack.get()
            if sym == '+':
                stack.put(b + a) 
            if sym == '-':
                stack.put(b - a)
            if sym == '*':
                stack.put(b * a)
            if sym == '/':
                if a == 0:
                    return -4
                stack.put(b / a)
    return stack.get()


print("Введите математическое выражение:")

math = str(input())
math = math.replace('=', '')
operation = ['+', '-', '*', '/']
r = []


result = brakets(math)
if result == -1:
    print('Первая входящая скобка - закрывающая')
    sys.exit()
elif result == -2:
    print('Существует не закртыая скобка')
    sys.exit()
elif result == -3:
    print('Закрывающая скобка ничего не закрывает')
    sys.exit()


result = data(math)
if result == -5:
    print('В выражении присутсвует неподходящий символ')
    sys.exit()
elif result == -6:
    print('В выражении недостаочно символов')
    sys.exit()
elif result == -7:
    print('В выражениие недостаточно чисел')
    sys.exit()
elif result == -8:
    print('В выражениие недостаточно операций')
    sys.exit()

result = rpn(result)

result = evaluate(result)

if result == -4:
    print('Делить на ноль нельзя')
    sys.exit()
else:
    print(result)





