import time
import keyboard


# =========== VERSION 2.0 ==============

last_dirc = "right"

places = {
    "up" : ["0","0","0","0","0","0","0","0","0"],
    "mid2" : ["0","0","0","0","0","0","0","0","0"],
    "mid" : ["0","0","0","0","0","0","0","0","0"],
    "down" : ["0","0","0","0","0","0","0","0","0"],
}

def Showplaces():
    for p in places:
        print(" ".join(places[p]))


def Direction():
    global last_dirc
    if keyboard.is_pressed('D'):
        last_dirc = "right"
    elif keyboard.is_pressed('A'):
        last_dirc = "left"
    elif keyboard.is_pressed('S'):
        last_dirc = "right"
    elif keyboard.is_pressed("W"):
        last_dirc = "right"
    return last_dirc

def search_rl():
    for p in places:
        if "1" in places[p]:
            return [p , places[p].index("1")]

def moves():
    direction = Direction()
    local = search_rl()[0]
    indx = search_rl()[1]
    if direction == "right":
        if places[local][indx + 1] == "0":
            places[local][indx] = "0"
            places[local][indx + 1] = "1"
    elif direction == "left":
        if places[local][indx - 1] == "0":
            places[local][indx] = "0"
            places[local][indx - 1] = "1"
           
print("=== SNAKE GAME ===\n1- Start\n2- Points")
choice = input("> ")
if choice == "1":
    places["down"][4] = "1"
    while True:
        moves()
        Showplaces()
        print("==================================")
        time.sleep(1)
        


