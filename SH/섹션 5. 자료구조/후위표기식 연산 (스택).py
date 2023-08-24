import sys
sys.stdin = open('input.txt','r')

eq = input()
stack = []

for e in eq :
    # number
    if e.isdecimal():
        stack.append(int(e))
    # operators
    else :
        n1 = stack.pop()
        n2 = stack.pop()
        if e == '+' :
            res = n2 + n1
        elif e == '-' :
            res = n2 - n1
        elif e == '*' :
            res = n2 * n1
        else :
            res = n2 / n1
        stack.append(res)

print(stack[0])