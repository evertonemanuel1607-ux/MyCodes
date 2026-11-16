valores = {
    "1" : "I",
    "2" : "II",
    "3" : "III",
    "4" : "IV",
    "5" : "V",
    "6" : "VI",
    "7" : "VII",
    "8" : "VIII",
    "9" : "IX",
    "10" : "X"
}

# primeiro prblema: Como maquina vai interpretar os valores (separar)

def calcular_sec(ano_out):
    ano_out = list(str(ano_out))
    if len(ano_out) == 3:
        if int(ano_out[len(ano_out) - 1]) >= 1:
            return int(ano_out[0]) + 1  
        else:
            return int(ano_out[0])
    elif len(ano_out) == 4:
        ano_out[0] = ano_out[0] + ano_out[1]
        ano_out.pop(1)
        if int(ano_out[len(ano_out) - 1]) >= 1:
            return int(ano_out[0]) + 1  
        else:
            return int(ano_out[0])

        
def converter(num):
    print("em desenvolvimento...")

   



ano = int(input("Ano: "))

print(f"Século: {converter(calcular_sec(ano))}")