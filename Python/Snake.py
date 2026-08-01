import time
import keyboard
import random
import os

# =========== VERSION 2.0 ==============

# Direction is right now, and system of points.

last_dirc = "right"
points = 0

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
        last_dirc = "down"
    elif keyboard.is_pressed("W"):
        last_dirc = "up"
    return last_dirc

def search_rl():
    for p in places:
        if "1" in places[p]:
            return [p , places[p].index("1")]

def next_up(place_now):
    next = {"down" : "mid","mid":"mid2","mid2" : "up", "up" : "down"}
    return next[place_now]

def next_down(place_now):
    next = {"up" : "mid2","mid2":"mid","mid":"down","down" : "up"}
    return next[place_now]

def setapple():
    valorrandom = random.randint(0,8)
    places_random = random.choice(["up","mid2","mid","down"])
    return [valorrandom,places_random]



def moves():
    global points,local_a,ind_a
    direction = Direction()
    local,indx = search_rl()
    if direction == "right":
        if places[local][indx + 1] == "0":
            places[local][indx] = "0"
            places[local][indx + 1] = "1"
        elif places[local][indx + 1] == "2":
            places[local][indx] = "0"
            places[local][indx + 1] = "1"
            points += 10
    elif direction == "left":
        if places[local][indx - 1] == "0":
            places[local][indx] = "0"
            places[local][indx - 1] = "1"
        elif places[local][indx - 1] == "2":
            places[local][indx] = "0"
            places[local][indx - 1] = "1"
            points += 10
    elif direction == "up":
        if places[next_up(local)][indx] == "0":
            places[local][indx] = "0"
            places[next_up(local)][indx] = "1"
        elif places[next_up(local)][indx] == "2":
                    places[local][indx] = "0"
                    places[next_up(local)][indx] = "1"
                    points += 10
    elif direction == "down":
            if places[next_down(local)][indx] == "0":
                places[local][indx] = "0"
                places[next_down(local)][indx] = "1"
            elif places[next_down(local)][indx] == "2":
                places[local][indx] = "0"
                places[next_down(local)][indx] = "1"
                points =+ 10
    if local == local_a and indx == ind_a:
        ind_a, local_a = setapple()
        places[local_a][ind_a] = "2"


print("=== SNAKE GAME ===\nINFO: Number one is Snake and Number 2 is the food Snake!\n1- Start\n2- Points")
choice = input("> ")
if choice == "1":
    places["down"][3] = "1"
    ind_a, local_a = setapple()
    places[local_a][ind_a] = "2"
    while True:
        os.system("cls")
        moves()
        Showplaces()
        print(f"==================================\nTotal Points: {points}")
        time.sleep(1)