# Funkcija za izračun Jaro-Winklerjeve razdalje
# Vhod: dva niza poljubnih velikosti
# Izhod: vrednost Jaro-Winklerjeve razdalje

def jaro_winkler(a, b, l, p=0.1):
    j = jaro(a, b)
    
    distance = j + l * p * (1 - j)
    
    return distance