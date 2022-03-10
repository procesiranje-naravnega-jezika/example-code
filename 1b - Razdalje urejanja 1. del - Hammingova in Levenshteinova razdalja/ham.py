# Funkcija za izračun Hammingove razdalje
# Vhod: dva niza istih velikosti
# Izhod: vrednost Hammingove razdalje

def ham(a, b):
    # če sta niza različnih dolžin, potem Hammingove razdalje ne moremo izračunati, zato vrnemo -1 
    if(len(a) != len(b)):
        return -1
    
    distance = 0 
    
    # prehod čez vsak znak v nizu
    for n in range(len(a)): 
        # če sta istoležna znaka različna, povečaj vrednost razdalje
        if(a[n] != b[n]):
            distance += 1
    return distance