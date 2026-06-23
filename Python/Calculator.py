total = 0

def sum(num):
    global total
    for n in num:
        total += n
        

def sub(num):
    global total
    for n in num:
        total -= n
    
def mult(num):
    global total
    if total == 0:
        total = 1
    for n in num:
        total *= n

def div(num):
    global total
    if total == 0:
        total = 1
    for n in num:
        total /= n

while True:
    print(f"Value: {total}")
    numbers = list(map(int,input("").split()))
    operacao = input("+ - * /\n> ")
    if operacao == "+":
        sum(numbers)
    elif operacao == "-":
        sub(numbers)
    elif operacao == "*":
        mult(numbers)
    elif operacao == "/":
        div(numbers)