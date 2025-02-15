# pip install git+https://github.com/PrithivirajDamodaran/Styleformer.git
from styleformer import Styleformer
import torch
import warnings
warnings.filterwarnings("ignore")

'''
#uncomment for re-producability
def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1234)
'''

# style = [0=Casual to Formal, 1=Formal to Casual, 2=Active to Passive, 3=Passive to Active etc..]
sf = Styleformer(style = 0) 

source_sentences = [
"I am quitting my job",
"Jimmy is on crack and can't trust him",
"What do guys do to show that they like a gal?",
"i loooooooooooooooooooooooove going to the movies.",
"That movie was fucking awesome",
"My mom is doing fine",
"That was funny LOL" , 
"It's piece of cake, we can do it",
"btw - ur avatar looks familiar",
"who gives a crap?",
"Howdy Lucy! been ages since we last met.",
"Dude, this car's dope!",
"She's my bestie from college",
"I kinda have a feeling that he has a crush on you.",
"OMG! It's finger-lickin' good.",
]   

for source_sentence in source_sentences:
    target_sentence = sf.transfer(source_sentence)
    print("-" *100)
    print("[Casual] ", source_sentence)
    print("-" *100)
    if target_sentence is not None:
        print("[Formal] ",target_sentence)
        print()
    else:
        print("No good quality transfers available !")