def mincost(km):
    cost=0
    if km>75:
        return km*8
    else:
        if km<=3:
            cost+=50
        elif km>3 and km<=18:
            cost+=50
            cost+=(km-3)*10
        else:
            cost+=(50)
            cost+=15*(10)
            cost+=(km-18)*8
    return cost
def sedan(km):
    cost=0
    if km>100:
        return km*10
    else:
        if km<=5:
            cost+=80
        elif km>5 and km<=20:
            cost+=80
            cost+=(km-5)*12
        else:
            cost+=(80)
            cost+=15*(12)
            cost+=(km-20)*10
    return cost
def suv(km):
    cost=0
    if km<=5:
        cost+=100
    elif km>5 and km<=20:
        cost+=100
        cost+=(km-5)*15
    else:
        cost+=100
        cost+=15*15
        cost+=(km-20)*12
    return cost 

km=int(input())
print("Mini - Rs. {}, Sedan - Rs.{} , SUV - Rs. {}".format(mincost(km),sedan(km),suv(km)))

