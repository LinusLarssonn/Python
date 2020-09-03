import math

ingredienser = ["smör", "ströbröd", "ägg", "strösocker", "vanlijsocker", "bakpulver", "vetemjöl", "smör", "vatten"]
mängdDelat4 = [2.5, 18.75, 0.75, 0.75, 0.5, 0.5, 0.75, 18.75, 0.25]
enhet = ["g", "ml", "st", "dl", "tsk", "tsk", "dl", "g", "dl"]

def recept(antal):
    i = 0

    for i in range(i, len(mängdDelat4)):
        mängdDelat4[i] = mängdDelat4[i] * antal
        if i == 0:
            print("")
            print("Till formen: ")
        if i == 2:
            print("")
            print("Till kakan: ")
            print (int(mängdDelat4[i]), enhet[i], ingredienser[i])
            i += 1
            continue
        print (mängdDelat4[i], enhet[i], ingredienser[i])
        i += 1

def tidBlanda(antal):
    standardTid = 10
    tid = standardTid + antal
    return tid

def tidGradda(antal):
    standardTid = 30
    tid = standardTid + antal * 3
    return tid

def sockerkaka(antal):
    recept(antal)
    totalTid = tidBlanda(antal) + tidGradda(antal)
    print("")
    print("Den totala tidsåtgången blir", totalTid, "minuter.")
    print("")

sockerkaka(9999999999999)





