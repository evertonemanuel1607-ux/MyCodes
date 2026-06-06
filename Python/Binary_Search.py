list_num = [1,3,5,7,9,11]

def search(item,listv):
    maxv = len(list_num) - 1
    minv = 0
    while minv <= maxv:
        center = (maxv + minv) // 2
        kick = listv[center]
        if kick == item:
            return center
        elif kick < item:
            minv = center + 1
        else:
            maxv = center - 1
    return None

print(search(3,list_num))
print(search(11,list_num))
print(search(4,list_num))