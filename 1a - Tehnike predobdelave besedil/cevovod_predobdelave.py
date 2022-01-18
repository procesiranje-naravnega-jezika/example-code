# cevovod
from gensim import utils
from pprint import pprint
import nltk
from nltk.corpus import stopwords
import lemmagen.lemmatizer
from lemmagen.lemmatizer import Lemmatizer

# spodnja vrstica se izvede samo prvič, da se v popolnosti prenese knjižnica NLTK
#nltk.download()

# 1. vhodno besedilo 
text = "Popili so bili ravnokar popoldansko kavo: prazne steklenice so bile še na mizi, pogrnjeni z nedeljskim prtom."
print("\n\nVHODNO BESEDILO")
pprint(text)
#print("\nsize="+str(len(text)))


# 2. tokenizacija in prečiščevanje
print("\n\nTOKENIZACIJA IN PREČIŠČEVANJE")
tokens = utils.simple_preprocess(text, deacc=False, min_len=3, max_len=15)
pprint(tokens)
#print("\nsize="+str(len(tokens)))

# 3. odstranjevanje blokiranih besed
print("\n\nODSTRANJEVANJE BLOKIRANIH BESED")
stop = stopwords.words('slovene')

filtered = [word for word in tokens if word not in stop]
pprint(filtered)
#print("\nsize="+str(len(filtered)))

# 4. lematizacija
print("\n\nLEMATIZACIJA")
lemmatizer = Lemmatizer(dictionary=lemmagen.DICTIONARY_SLOVENE)
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
pprint(lemmatized)
#print("\nsize="+str(len(lemmatized)))