# Funkcija za izračun Jarove razdalje
# Vhod: dva niza poljubnih velikosti
# Izhod: vrednost Jarove razdalje

def jaro(a, b):
    distance = 0 
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
    
    # znaka se ujemata, če sta enaka in sta oddaljena največ v obsegu, ki ga izračunamo spodaj
    match_range = (max(len_a, len_b) // 2 ) - 1
    
    #print('primerjalno okno: ', match_range)
    
    # pomožni polji boolovih spremenljivk, ki ponazarjata znakovna ujemanja; inicializiramo na vrednost False
    matches_a = [False] * len_a
    matches_b = [False] * len_b
    
    m = 0 # število ujemajočih znakov
    t = 0 # število transpozicij
    
    # vsak znak iz a primerjamo z vsemi ujemajočimi znaki v b
    for i in range(len_a):
        
        # začetek in konec primerjalnega okna
        start = max(0, i - match_range) 
        end = min(i + match_range + 1, len_b)
        
        for j in range(start, end):
            # če imamo ujemanje v b, nadaljujemo
            if(matches_b[j]):
                continue
            
            if(a[i] != b[j]):
                continue
            
            # sicer nastavimo True v pomožnih poljih in povečamo število ujemanj ter končamo pregled znotraj primerjalnega okna
            matches_a[i] = True
            matches_b[j] = True
            m += 1
            break

        # če ni ujemanj, potem bo razdalja enaka 0
        if(m == 0):
            distance = 0

    #print(a, '->', matches_a)
    #print(b, '->', matches_b)
            
    # transpozicije
    k = 0
    for i in range(len_a):
        if not matches_a[i]:
            continue
        while not matches_b[k]:
            k += 1
        if(a[i] != b[k]):
            t += 1
        k +=1
    
    #print('ujemanja: ', m)
    #print('transpozicije: ', t)
    
    distance = ((m / len_a) + (m / len_b) + ((m - (t / 2)) / m)) / 3.0
        
    return distance