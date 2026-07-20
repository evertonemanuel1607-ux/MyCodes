import time
import keyboard

points = 0

places = {
    "up" : ["0","0","0","0","0","0","0","0","0"],
    "mid" : ["0","0","0","0","0","0","0","0","0"],
    "mid2" : ["0","0","0","0","0","0","0","0","0"],
    "down" : ["0","0","0","0","0","0","0","0","0"]
}

def keyboard_read():
    if keyboard.is_pressed("A"): # Preciso de uma manneira de manter o resultado da última aplicação, para assim ele posso continuar percorrer
        d = "left"
    elif keyboard.is_pressed("D"):
        d = "right"
    return d

def show_places():
    for p in places:
        print(" ".join(places[p]))

def walk():
    for p in places:
        try:
            if "1" in places[p] and keyboard_read() == "right":
                ind = places[p].index("1")
                if places[p][ind + 1] == "0":
                    places[p][ind] = "0"
                    places[p][ind + 1] = "1"
            elif "1" in places[p] and keyboard_read() == "left":
                ind = places[p].index("1")
                if places[p][ind - 1] == "0":
                    places[p][ind] = "0"
                    places[p][ind - 1] = "1"
        except IndexError:
            places[p][0] = "1"
            places[p][ind] = "0"



print("=== Snake ===\n1- Start?\n2- Points")
options = input("> ")
if options == "1":
    places["mid2"][4] = "1"
    while True:
        show_places()
        print("_____________________________")
        walk()
        time.sleep(1.2)

    

