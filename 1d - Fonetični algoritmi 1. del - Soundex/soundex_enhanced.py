# implementacija izboljšanega algoritma Soundex
def soundex_enhanced(input):
  word = ''
  sdx = ''

  if (input is None or not input or input == ''):
    return None
  
  # 1.: pretvorba vseh črk v velike tiskane črke
  word = input.upper()

  # 2.: pretvorba šumnikov ĆČŠŽ => CCSZ
  replace_chars = {'Ć': 'C', 'Č': 'C', 'Š': 'S', 'Ž': 'Z'}
  word = ''.join([replace_chars.get(c, c) for c in word])

  # 3.: ohranjanje prve črke
  sdx += word[0]

  # 4.: preslikava črk
  soundex_map = {
      'AEIOUHWY': '.',    # samoglasniki AEIOU in črke H, W ter Y se izključijo (označimo jih z znakom '.')
      'BP': '1',          # črki B in P se preslikata v 1; izboljšava
      'FV': '2',          # črki F in V se preslikata v 2; izboljšava
      'CSK': '3',         # črke C, S in K se preslikajo v 3; izboljšava
      'GJ': '4',          # črki G in J se preslikata v 4; izboljšava
      'QXZ': '5',         # črke Q, X in Z se preslikajo v 5; izboljšava
      'DT': '6',          # črki D in T se preslikata v 6
      'L': '7',           # črka L se preslika v 7
      'MN': '8',          # črki M in N se preslikata v 8
      'R': '9'            # črka R se preslika v 9
  }

  # izvedba preslikave
  for c in word[1:]:                # za vse črke razen prve
    for key in soundex_map.keys():  # za vse vrednosti preslikave
      if(c in key):                  # če je črka prisotna v ključu za preslikavo
        code = soundex_map[key]     # dodeli vrednost ključa

        # če vrednost ni samoglasnik in ni enaka zadnji vrednosti preslikave (s tem izničimo ponavljajoče znake: npr. Manning smatramo kot Maning)
        if(code != '.' and code != sdx[-1]):
          sdx += code             # dodamo vrednost v rezultat

  # 5.: vrednost Soundex mora biti velika 4 znake; če je manjša dodamo ničle na konec
  sdx = sdx[:4].ljust(4, '0')

  return sdx