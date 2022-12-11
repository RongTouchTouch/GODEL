from nltk.tokenize import sent_tokenize
tot = []
with open('full_speech.txt','r') as f:
    # a line is a speech -> split
    ss = f.readlines() # list[str]
    for s in ss: # s is string
        token_text = sent_tokenize(s) #list[str]
        tot += token_text   

# delete [***]
import re
for i in range(len(tot)):
    tot[i] = re.sub(r'\[(?:[^|\]]*\|)?([^\]]*)]','',tot[i])
    tot[i] = tot[i].replace('......',' ')
    tot[i] = tot[i].lstrip()
    tot[i] = tot[i].rstrip()
    
# delete sent too short
lines = []
for s in tot:
    if(len(s.split(' ')) >= 3):
        lines.append(s)  

# delete
    
with open('origin.txt', 'w') as f:
    for line in lines:
        f.write(f"{line}\n")