import math
def cal_watts(I, V):
    # print(I, V, R)
    if I != "None" and V != "None" or I != "" and V != "" or I != "0" and V != "0":
        I = I
        V = V
        P = I * V
        return P


def cal_volts(I, P):
    if I != "None" and P != "None" or I != "" and P != "" or I != "0" and P != "0":
        I = I
        P = P
        V = P / I
        return V


def cal_amperes(V, P):

    if P != "None" and V != "None" or P != "" and V != "" or P != "0" and V != "0":
        V = V
        P = P
        I = P / V
        return I




def cal_kiloWatt(P):
    kW = P / 1000
    return kW

def cal_kiloVoltamps(I, V):
    s = V / 1000
    SkVA = I * s
    return SkVA

def cal_vaone(I, V):
    va = I * V
    return va

def cal_vathree(I, V):
    va = math.sqrt(3) * I * V
    return va

def cal_vaampone(VA, V, Op):

    if Op == 'three':
        i = math.sqrt(3) * V
        amps = VA / i
        return amps
    else:
        amps = VA / V
        return amps

def cal_kvaampone(KVA, V, Op):

    if Op == 'three':
        i = 1000 * KVA
        j = math.sqrt(3) * V
        amps = i / j
        return amps
    else:
        i = 1000 * KVA
        amps = i / V
        return amps

def cal_ampkvaone(I, V, Op):

    if Op == 'three':
        i = math.sqrt(3) * V * I
        kva = i / 1000
        return kva
    else:
        i = V * I
        kva = i / 1000
        return kva

def cal_wjoule(P ,S):
    J = P * S
    return J
