import time
import keyboard

points = 0
d = "right"

places = {
    "up" : ["0","0","0","0","0","0","0","0","0"],
    "mid" : ["0","0","0","0","0","0","0","0","0"],
    "mid2" : ["0","0","0","0","0","0","0","0","0"],
    "down" : ["0","0","0","0","0","0","0","0","0"]
}

def keyboard_read():
    global d
    if keyboard.is_pressed("A"): # Preciso de uma manneira de manter o resultado da última aplicação, para assim ele posso continuar percorrer
        d = "left"
    elif keyboard.is_pressed("D"):
        d = "right"
    elif keyboard.is_pressed("W"):
        d = "up"
    elif keyboard.is_pressed("S"):
        d = "down"
    return d

def show_places():
    for p in places:
        print(" ".join(places[p]))

def where_up(postion):
    if postion == "down":
        return "mid2"
    elif postion == "mid2":
        return "mid"
    elif postion == "mid":
        return "up"
    elif postion == "up":
        return "down"
    
def where_down(postion):
    if postion == "down":
        return "up"
    elif postion == "mid2":
        return "down"
    elif postion == "mid":
        return "mid2"
    elif postion == "up":
        return "mid"

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
            elif "1" in places[p] and keyboard_read() == "up":
                ind = places[p].index("1")
                if places[where_up(p)][ind] == "0":
                    places[p][ind] = "0"
                    places[where_up(p)][ind] = "1"
            elif "1" in places[p] and keyboard_read() == "down":
                ind = places[p].index("1")
                if places[where_down(p)][ind] == "0":
                    places[p][ind] = "0"
                    places[where_down(p)][ind] = "1"
                    
            
        except IndexError:
            places[p][0] = "1"
            places[p][ind] = "0"



print("=== Snake ===\n1- Start?\n2- Points")
options = input("> ")
if options == "1":
    places["down"][4] = "1"
    while True:
        show_places()
        print("_____________________________")
        time.sleep(1.5)
        walk()
        

    

