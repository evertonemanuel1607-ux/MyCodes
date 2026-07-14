def fat(num):
    if num == 1:
        return num
    return fat(num - 1) * num

while True:
    print("=== Factorial ===")
    number = int(input("> "))
    if number == 0:
        break
    else:
        print(f"Factorial of {number} is: {fat(number)}")

print("Bye bye!")