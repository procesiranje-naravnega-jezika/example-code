# -*- coding: utf-8 -*-
"""WER_TER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZHDO-nVEET32Wt47_TS8DNzZuTgtKK4K
"""

import numpy as np

# Funkcija za izračun število premikov
# Vhod: dva niza poljubnih velikosti (v obliki polja)
# Izhod: število premikov

def premik(besede_a, besede_b):
  shift = 0

  i = 0
  while i < len(besede_a):
    for j in range(0, len(besede_b)):
      if i != j and besede_a[i] == besede_b[j]:

        moved_word = besede_a.pop(i)
        besede_a.insert(j, moved_word)
        shift = shift + 1
        reset = True
        break
      else:
        reset = False

    if reset == True:
      i = 0
    else:
      i = i + 1

  return besede_a, shift

# Funkcija za izračun Levenshteinove razdalje za besede
# Vhod: dva niza poljubnih velikosti, premik (opcijsko)
# Izhod: vrednost Levenshteinove razdalje

def lev(a, b, op_premik=False):
    besede_a = a.split()
    besede_b = b.split()

    rows = len(besede_a) + 1
    cols = len(besede_b) + 1

    shift = 0
    if op_premik == True:
      besede_a, shift = premik(besede_a, besede_b)

    # inicializacija pomožne matrike
    distances = np.zeros((rows, cols))

    for i in range(1, rows):
        distances[i, 0] = i

    for j in range(1, cols):
        distances[0, j] = j

    # izračun vrednosti elementov pomožne matrike
    for i in range(1, rows):
        for j in range(1, cols):
            # če sta besedi enaki, potem je vrednost elementa enaka vrednosti zgornjega levega diagonalnega elementa
            if(besede_a[i - 1] == besede_b[j - 1]):
                distances[i, j] = distances[i - 1, j - 1]

            # če znaka nista enaka, potem je vrednost elementa enaka minimalni vrednosti sosednih elementov (levega, levega diagonalnega in zgornjega) + 1
            else:
                distances[i, j] = min(distances[i - 1, j - 1], distances[i - 1, j], distances[i, j - 1]) + 1

    # izpis izračunanih vrednosti pomožne matrike
    print(distances)

    # vrednost Levenshteinove razdalje je v skrajnem spodnjem desnem elementu pomožne matrike
    return distances[rows - 1, cols - 1] + shift

# Funkcija za izračun podobnosti po metriki WER
# Vhod: dve povedi poljubnih velikosti
# Izhod: vrednost podobnosti na intervalu [0, 100]

def sim_WER(referenca, prevod):

    d = lev(referenca, prevod)
    similarity = d / len(referenca.split())
    similarity *= 100
    print('Podobnost (WER): ', similarity)
    return similarity

# Funkcija za izračun podobnosti po metriki TER
# Vhod: dve povedi poljubnih velikosti
# Izhod: vrednost podobnosti na intervalu [0, 100]

def sim_TER(referenca, prevod):

    d = lev(referenca, prevod, True)
    similarity = d / len(referenca.split())
    similarity *= 100
    print('Podobnost (TER): ', similarity)
    return similarity

referenca = 'danes je lep dan'
prevod = 'lep dan je danes'
#prevod = 'danes je slab dan'
#prevod = 'lep dan je danes'
#prevod = 'danes ni dan je'

sim_WER(referenca, prevod)

sim_TER(referenca, prevod)

