import numpy as np

# Funkcija za izračun Levenshteinove razdalje
# Vhod: dva niza poljubnih velikosti
# Izhod: vrednost Levenshteinove razdalje

def lev(a, b):
    rows = len(a) + 1
    cols = len(b) + 1
    
    # inicializacija pomožne matrike
    distances = np.zeros((rows, cols))
    
    for i in range(1, rows):
        distances[i, 0] = i
        
    for j in range(1, cols):
        distances[0, j] = j
    
    # izračun vrednosti elementov pomožne matrike
    for i in range(1, rows):
        for j in range(1, cols):
            # če sta znaka enaka, potem je vrednost elementa enaka vrednosti zgornjega levega diagonalnega elementa 
            if(a[i - 1] == b[j - 1]):
                distances[i, j] = distances[i - 1, j - 1]
            
            # če znaka nista enaka, potem je vrednost elementa enaka minimalni vrednosti sosednih elementov (levega, levega diagonalnega in zgornjega) + 1
            else:
                distances[i, j] = min(distances[i - 1, j - 1], distances[i - 1, j], distances[i, j - 1]) + 1
    
    # izpis izračunanih vrednosti pomožne matrike
    print(distances)
    
    # izpis zaporedja operacij
    PrintEditOperations(distances, a, b)
    
    # vrednost Levenshteinove razdalje je v skrajnem spodnjem desnem elementu pomožne matrike
    return distances[rows - 1, cols - 1]


def PrintEditOperations(distances, a, b):
    print("Za pretvorbo niza '" + a + "' v niz '" + b + "', velja naslednje zaporedje operacij:")
    
    # prehod poteka od skrajnega spodnjega desnega elementa pomožne matrike
    i = distances.shape[0] - 1
    j = distances.shape[1] - 1
    
    while(True):
        # pogoj za zaključek prehoda je, kadar pridemo v skrajni zgornji levi element pomožne matrike
        if(i == -1 or j == -1):
            break;
            
        # če sta znaka enaka, potem operacija ni potrebna in se premaknemo levo diagonalno
        if(a[i - 1] == b[j - 1]):
            i = i - 1
            j = j - 1

        # če znaka nista enaka, preverimo ali gre za zamenjavo (ali je trenutna vrednost enaka vrednosti zgoraj levo + 1?)
        elif(distances[i, j] == distances[i - 1, j - 1] + 1):
            print("zamenjava znaka '" + a[i - 1] + "' z znakom '" + b[j - 1] + "'")
            i = i - 1
            j = j - 1
            
        # če znaka nista enaka, preverimo ali gre za brisanje (ali je trenutna vrednost enaka vrednosti zgoraj + 1?)    
        elif(distances[i, j] == distances[i - 1, j] + 1):
            print("brisanje znaka '" + a[i - 1] + "'")
            i = i - 1
            
        # če znaka nista enaka, preverimo ali gre za vstavljanje (ali je trenutna vrednost enaka vrednosti levo + 1?)    
        elif(distances[i, j] == distances[i, j - 1] + 1):
            print("vstavljanje znaka '" + b[j - 1] + "'")
            j = j - 1
        
        # sicer smo na koncu in prekinemo izvajanje zanke
        else:
            break

# Funkcija za izračun Levenshteinove podobnosti
# Vhod: dva niza poljubnih velikosti
# Izhod: vrednost Levenshteinove podobnosti na intervalu [0, 1]

def sim_lev(a, b):
    a_len = len(a)
    b_len = len(b)
    
    d = lev(a, b)
    print('Levenshteinova razdalja: ', d)
    similarity = ((a_len + b_len) - d)/(a_len + b_len)
    return similarity