# implementacija algoritma Caverphone 2.0
import string

def caverphone2(input):
  cvphn = ''
  word = ''

  if(input is None or not input or input == ''):
    return None

  # 1.: pretvorba v male črke
  word = input.lower()

  # 2.: odstrani vse, kar ni v standardni abecedi
  for c in word:
    if(c not in string.ascii_lowercase):
      word = word.replace(c, '')

  # 3.: odstrani 'e' na koncu besede
  if(word.endswith('e')):
    word = word.removesuffix('e')

  # 4.: preslikava '*ough' in 'gn' v '2f' in '2n'
  ough_gn_map = {
      'cough': 'cou2f',
      'rough': 'rou2f',
      'tough': 'tou2f',
      'enough': 'enou2f',
      'trough': 'trou2f',
      'gn': '2n'
  }

  for key in ough_gn_map.keys():
    if(word.startswith(key)):
      word = word.replace(key, ough_gn_map[key])

  # 5.: preslikava 'mb' v 'm2'
  if(word.endswith('mb')):
    word = word.removesuffix('mb') + 'm2'

  # 6.: dodatne preslikave znakov (1-17)
  map_1_17 = {
      'cq': '2q',     # 1
      'ci': 'si',     # 2
      'ce': 'se',     # 3
      'cy': 'sy',     # 4
      'tch': '2ch',   # 5
      'c': 'k',       # 6
      'q': 'k',       # 7
      'x': 'k',       # 8
      'v': 'f',       # 9
      'dg': '2g',     # 10
      'tio': 'sio',   # 11
      'tia': 'sia',   # 12
      'd': 't',       # 13
      'ph': 'fh',     # 14
      'b': 'p',       # 15
      'sh': 's2',     # 16
      'z': 's',       # 17
  }

  for key in map_1_17.keys():
    word.replace(key, map_1_17[key])

  # 7.: dodatne preslikave znakov (18-19)
  # samoglasniki so definirani z algoritmom
  vowels = ['a','e','i','o','u','æ','ā','ø']
  # > 18 - vsak prvi samoglasnik postane 'A'
  # > 19 - vsi ostali samoglasniki postanejo '3'
  tmp = ''
  for i, c in enumerate(word):
    if(c in vowels):
      tmp += 'A' if(i == 0) else '3'
    else:
      tmp += c

  word = tmp

  # 7.1.: dodatne preslikave znakov (20)
  # > 20 - 'j' postane 'y'
  word = word.replace('j', 'y')

  # 7.2.: dodatne preslikave znakov (21-22)
  # > 21 - začetni 'y3' postane 'Y3'
  if(word.startswith('y3')):
    word = word.replace('y3', 'Y3', 1)

  # > 22 - začetni 'y' postane 'A'
  if(word.startswith('y')):
    word = word.replace('y', 'A', 1)

  # 7.3.: dodatne preslikave znakov (23)
  # > 23 - 'y' postane '3'
  word = word.replace('y', '3')

  # 7.3.: dodatne preslikave znakov (24)
  # > 24 - '3gh3' postane '3kh3'
  word = word.replace('3gh3', '3kh3')

  # 7.4.: dodatne preslikave znakov (25)
  # > 25 - 'gh' postane '22'
  word = word.replace('gh', '22')

  # 7.5.: dodatne preslikave znakov (26)
  # > 26 - 'g' postane 'k'
  word = word.replace('g', 'k')

  # 7.6.: dodatne preslikave znakov (27-33)
  # določene grupirane male črke se postanejo velika črka
  # > 27 - 'sss...' postane 'S'
  # > 28 - 'ttt...' postane 'T'
  # > 29 - 'ppp...' postane 'P'
  # > 30 - 'kkk...' postane 'K'
  # > 31 - 'fff...' postane 'F'
  # > 32 - 'mmm...' postane 'M'
  # > 33 - 'nnn...' postane 'N'

  adjacent_chars = ['s', 't', 'p', 'k', 'f', 'm', 'n']
  tmp = ''
  for i, c in enumerate(word):
    if(c in adjacent_chars):
      upper_c = c.upper()
      if(len(tmp) > 0 and tmp[-1] == upper_c):
        continue
      tmp += upper_c
      continue
    tmp += c

  word = tmp

  # 7.7.: dodatne preslikave znakov (34)
  # > 34 - 'w3' postane 'W3'
  word = word.replace('w3', 'W3')

  # 7.8.: dodatne preslikave znakov (35)
  # > 35 - 'wh3' postane 'Wh3'
  word = word.replace('wh3', 'Wh3')

  # 7.9.: dodatne preslikave znakov (36)
  # > 36 - če se beseda konča z 'w', zamenjaj zadnji 'w' s '3'
  if(word.endswith('w')):
    word = word.removesuffix('w') + '3'

  # 7.10.: dodatne preslikave znakov (37)
  # > 37 - 'w' postane '2'
  word = word.replace('w', '2')

  # 7.11.: dodatne preslikave znakov (38)
  # > 38 - vsak začetni 'h' postane 'A'
  if(word.startswith('h')):
    word = word.removeprefix('h') + 'A'

  # 7.12.: dodatne preslikave znakov (39)
  # > 39 - vsi preostali 'h' postanejo '2'
  word = word.replace('h', '2')

  # 7.13.: dodatne preslikave znakov (40)
  # > 40 - 'r3' postane 'R3'
  word = word.replace('r3', 'R3')

  # 7.14.: dodatne preslikave znakov (41)
  # > 41 - če se beseda konča z 'r', zadnji 'r' postane '3'
  if(word.endswith('r')):
    word = word.removesuffix('r') + '3'

  # 7.15.: dodatne preslikave znakov (42)
  # > 42 - 'r' postane '2'
  word = word.replace('r', '2')

  # 7.16.: dodatne preslikave znakov (43)
  # > 43 - 'l3' postane 'L3'
  word = word.replace('l3', 'L3')

  # 7.17.: dodatne preslikave znakov (44)
  # > 44 - če se beseda konča z 'l', zadnji 'l' postane '3'
  if(word.endswith('l')):
    word = word.removesuffix('l') + '3'

  # 7.18.: dodatne preslikave znakov (45)
  # > 45 - 'l' postane '2'
  word = word.replace('l', '2')

  # 8.: odstrani vse '2'
  word = word.replace('2', '')

  # 9.: če se beseda konča s '3', zadnja '3' postane 'A'
  if(word.endswith('3')):
    word = word.removesuffix('3') + 'A'

  # 10.: odstrani vse '3'
  word = word.replace('3', '')

  # 11-12.: dodaj deset enic na konec in vrni prvih deset znakov kot rezultat
  word = word.ljust(10, '1')

  return word