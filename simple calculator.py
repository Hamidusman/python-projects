def calc(a, b):
    if op =='+':
        return (a + b)
    elif op == '-':
        return (a - b)
    elif op =='/':
        return (a - b)
    elif op == '*':
        return (a * b)
    else:
        return('Invalid input, try again')

a = int(input('Enter A Number: '))
b = int(input('Enter A Number: '))
op = input('Select An Operator: ')

print( calc(a, b))


