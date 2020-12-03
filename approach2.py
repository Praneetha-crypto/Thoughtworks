mini_dict=dict()
sedan_dict=dict()
suv_dict=dict()
def mini(km):
    global minidict
    if km in mini_dict.keys():
        return mini_dict[n]
    res=0
    if km>75:
        res=km*8
    elif km>18:
        res+=200
        res+=(km-18)*8
    elif km<=18 and km>3:
        res+=50
        res+=(km-3)*10
    else: res=50
    return res
def sedan(km):
    global sedan_dict
    if km in sedan_dict.keys():
        return sedan_dict[n]
    res=0
    if km>100:
        res=km*10
    elif km>20:
        res+=80
        res+=(15*12)
        res+=(km-20)*10
    elif km<=20 and km>5:
        res=80+(km-5)*12
    else:
        res=80
    return res
def suv(km):
    global suv_dict
    if km in suv_dict.keys():
        return suv_dict[n]
    res=0
    if km<=5:
        res=100
    elif km>5 and km<=20:
        res+=100
        res+=(km-5)*15
    else:
        res=325+(km-20)*12
    return res
km=int(input())
print("Mini - Rs. {}, Sedan - Rs.{} , SUV - Rs. {}".format(mini(km),sedan(km),suv(km)))




