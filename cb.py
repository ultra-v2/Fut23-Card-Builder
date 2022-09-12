import os
import sys

#int pac, pac1, acc, sps
#int sho, pos, fin, shp, los, vol, pen
#int pas, vis, cro, fks, spa, lpa, cur
#int dri, agi, bal, rea, bac, drb, com
#int dfn, itr, hea, mar, stt, slt
#int phy, jum, sta, stn, agg
#int ovr, OVR

os.system('clear')

name = input("Name: ")
pos = input("Position(GK For GK):")

if poss == "GK" or "gk":
    div = int(input("Diving: "))
    han = int(input("Handling: "))
    kic = int(input("Kicking: "))
    ref = int(input("Reflex: "))
    spd = int(input("Speed: "))
    psi = int(input("Positioning: "))

    ovr2 = div + han + kic + ref + spd + psi
    ovr3 = ovr2 / 5.26

    print("OVR: ", int(ovr3))

    print("")
    print("-------------------")
    print(name, int(ovr3), pos)
    print("-------------------")
    print(int(div), " DIV | ", int(ref), " REF")
    print(int(han), " HAN | ", int(spd), " SPD")
    print(int(kic), " KIC | ", int(psi), " POS")

    sys.exit("Done")

print("PAC")
acc = int(input("Acceleration: "))
sps = int(input("Sprint Speed: "))
pac1 = acc + sps
pac = pac1 / 2
print("PAC: ", int(pac))

print("SHO")
pos = int(input("Possistioning: "))
fin = int(input("Finishing: "))
shp = int(input("Shot Power: "))
los = int(input("Long Shots: "))
vol = int(input("Volleys: "))
pen = int(input("Penalties: "))
sho1 = pos + fin + shp + los + vol + pen
sho = sho1 / 6
print("SHO: ", int(sho))

print("PAS")
vis = int(input("Vision: "))
cro = int(input("Crossing: "))
fks = int(input("Free Kicks: "))
spa = int(input("Short Passing: "))
lpa = int(input("Long Passing: "))
cur = int(input("Curve: "))
pas1 = vis + cro + fks + spa + lpa + cur
pas = pas1 / 6
print("PAS: ", int(pas))

print("DRI")
agi = int(input("Agility: "))
bal = int(input("Balance: "))
rea = int(input("Reactions: "))
bac = int(input("Ball Control: "))
drb = int(input("Dribbling: "))
com = int(input("Composure: "))
dri1 = agi + bal + rea + bac + drb + com
dri = dri1 / 6
print("DRI: ", int(dri))

print("DEF")
itr = int(input("Interceptions: "))
hea = int(input("Heading: "))
mar = int(input("Marking: "))
stt = int(input("Standing Tackle: "))
slt = int(input("Sliding Tackle: "))
def1 = itr + hea + mar + stt + slt
dfn = def1 / 5
print("DEF: ", int(dfn))

print("PHY")
jum = int(input("Jumping: "))
sta = int(input("Stamina: "))
stn = int(input("Strength: "))
agg = int(input("Aggresion: "))
phy1 = jum + sta + stn + agg
phy = phy1 / 4
print("PHY: ", int(phy))

ovr1 = pac + sho + pas + dri + dfn + phy
ovr = ovr1 / 5.26

print("OVR: ", int(ovr))

print("")
print("-------------------")
print(name, int(ovr), poss)
print("-------------------")
print(int(pac), " PAC | ", int(dri), " DRI")
print(int(sho), " SHO | ", int(dfn), " DEF")
print(int(pas), " PAS | ", int(phy), " PHY")
