import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def crds(cards):
    crd=random.choice(cards)
    return crd
cmd=[]
usd=[]

for _ in range(2):
    usd.append(crds(cards))
    cmd.append(crds(cards))

def srcalcul(crd):
    if sum(crd)==21 and len(crd)==2:
        return 0
    elif 11 in crd and sum(crd)>21:
        crd.remove(11)
        crd.append(1)
    return sum(crd)

usds=srcalcul(usd)
cmds=srcalcul(cmd)
def compare(usds,cmds):
    if usds> 21 and cmds>21 :
        return "blackjack : you lose"
    elif usds > 21:
        return "lose blackjk"
    elif cmds > 21:
        return"u win"
    elif cmds==0:
        return "u win"
    elif usds==0:
        return "u lose"
    elif usds==cmds:
        return"draw"
    elif usds>cmds:
        return" u win"
    else:
        return "u lose"

f=True
while f:
    usds = srcalcul(usd)
    print(f"your cards are {usd} and your score is : {usds}")
    print(f"the computer 1st card is : {cmd[0]}")
    if usds==0 or cmds==0 or usds>21:
        f=False
    else:
        x= input("do you wanna add another card , type 'y' or 'n' : ")
        if x == "y" :
            usd.append(crds(cards))
        else:
            f=False
while cmds!=0 and cmds<17:
        cmd.append(crds(cards))
        cmds = srcalcul(cmd)
print(f"your final cards are {usd} and your final score is : {usds}")
print(f"computer final cards are {cmd} and the score is : {cmds}")
print(compare(usds,cmds))





