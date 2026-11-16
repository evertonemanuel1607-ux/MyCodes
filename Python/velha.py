# Jogo da velha Version 1.0

import random

places_back = {
    "up" : ["_","_","_"],
    "mid" : ["_","_","_"],
    "down" : ["_","_","_"]
}

def showplaces():
    for p in places_back:
        print(places_back[p])


def turn_player(posicao,indice):
    if places_back[posicao][indice] != "O":
        places_back[posicao][indice] = "X"
    else:
        print("Local inválido...turno perdido...")
        return

def turn_bot():
    posicionar = False 
    while not posicionar:
        local = random.choice(["up","mid","down"])
        indice_place_bot = random.randint(0,2)
        if places_back[local][indice_place_bot] == "X" or places_back[local][indice_place_bot] == "O":
            pass 
        else:
            places_back[local][indice_place_bot] = "O"
            posicionar = True 

def the_game():
    finish = who_is_the_winner()
    while not finish:
        turn_bot()
        showplaces()
        place_choice = input("up, mid or down: ")
        indice_place = int(input("0 a 2: "))
        turn_player(place_choice,indice_place)
        finish = who_is_the_winner()
    showplaces()

def who_is_the_winner():
    if "_" not in places_back["up"] or "_" not in places_back["mid"] or "_" not in places_back["down"]:
        for p in places_back:
            if places_back[p] == ["O","O","O"] or places_back[p] == ["X","X","X"]:
                return True
    elif "X" in places_back["up"] or "O" in places_back["up"]:
        for i in range(3):
            if places_back["down"][i] == places_back["mid"][i] and places_back["mid"][i] == places_back["up"][i] and places_back["up"][i] is not "_":
                 return True

    


while True:
    print("=== Jogo da Véia ===\n1- Start\n2- Points\n3- LEIA")
    escolha = input("> ")
    if escolha == "1":
        print("Iniciando...Caso queira sair, coloque Z na primeira entrada...")
        the_game()
    elif escolha == "3":
        print("Existem 3 locais: up, mid e down que significam respectivamente cima, meio e baixo...\nQuando solicitado preencha o local de interesse.\n Caso selecione o local do bot, perderá o turno como penalização.\nos numeros simbolizam a posição, caso 0, significa a primeira de tal local.\nNão passe do limite!")
        