import math

input_ = 1
output_desire = int(input("0 or 1: "))

input_weight = 0.5 
learnig_rate = 0.1

def activation(su):
    if su >= 0:
        return 1
    else:
        return 0 

error = math.inf

while error != 0:
    sume = input_ * input_weight
    output = activation(sume)
    
    error = output_desire - output
    print(error)
    print(f"### Poder: {input_weight} \nAprendizado: {learnig_rate}\nSoma: {sume}")
    
    if not error == 0:
        input_weight = input_weight + ( learnig_rate * input_* error)

print("VAMO!")