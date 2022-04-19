# Funkcija za izračun Jarove razdalje
# Vhod: dva niza poljubnih velikosti
# Izhod: vrednost Jarove razdalje

import itertools
def jaro(a, b):
    # niz a je vedno daljši niz
    if(len(a) < len(b)):
        tmp = b
        b = a
        a = tmp
        
    #print('a=', a)
    #print('b=', b)
    
    # dolžini nizov a in b
    len_a = len(a) 
    len_b = len(b)
    
    # izračun primerjalnega okna
    window_size = (max(len_a, len_b) // 2) - 1
    #print('primerjalno okno: ', window_size)
    
    # pomožni polji boolovih spremenljivk, ki ponazarjata znakovna ujemanja; inicializiramo na vrednost False
    matches_a = [False] * len_a
    matches_b = [False] * len_b
    
    # spremenljivka m hrani število ujemanj
    m = 0
    
    # preverimo ujemanja s prehodom skozi niz a
    for i, char in enumerate(a):
        start = max(0, i - window_size)
        end = min(i + window_size + 1, len_b)
        
        for j, c in enumerate(b[start:end], start):
            
            # če imamo ponavljajoče ujemanje (ujemanje v enakem znaku), potem ne štejemo dvakrat
            if(matches_b[j]):
                continue
            
            # če imamo ujemanje
            if(c == char):
                # zabeležimo ujemanje v pomožnih poljih
                matches_a[i] = True
                matches_b[j] = True
                
                # povečamo število ujemanj
                m += 1
                break
           
    # če ni ujemanj, bo razdalja enaka 0
    distance = 0.0
    if(m == 0):
        return distance
    
    #print(a, '->', matches_a)
    #print(b, '->', matches_b)
        
    # sicer preverimo še transpozicije
    check_a = itertools.compress(a, matches_a)
    check_b = itertools.compress(b, matches_b)
    
    # izračunamo število transpozicij
    t = sum(x != y for x, y in zip(check_a, check_b))
    
    #print('ujemanja: ', m)
    #print('transpozicije: ', t)
    
    distance = ((m / len_a) + (m / len_b) + ((m - (t / 2)) / m)) / 3.0
    return distance 