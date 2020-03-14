import nltk
from nltk import word_tokenize

text_Eng =word_tokenize("What is this, I really don't know") 
# check (Pos) Part of Speech tag
output = nltk.pos_tag(text_Eng)
print(output)
