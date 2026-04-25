from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")
snape = Symbol("snape")

knowledge = And(
    Implication(Not(rain), hagrid),        # Rule 1: no rain → met Hagrid (unchanged)
    Or(hagrid, dumbledore, snape),         # Updated: at least one of the three
    Not(And(hagrid, dumbledore)),          # Not both hagrid and dumbledore
    Not(And(hagrid, snape)),               # Not both hagrid and snape
    Not(And(dumbledore, snape)),           # Not both dumbledore and snape
    dumbledore,                            # Fact: met Dumbledore (unchanged)
    Implication(rain, Not(snape)),         # New Rule: if raining → snape didn't come
    snape                                  # New Fact: Snape was seen outdoors
)

print("rain:", model_check(knowledge, rain))
print("hagrid:", model_check(knowledge, hagrid))
print("dumbledore:", model_check(knowledge, dumbledore))
print("snape:", model_check(knowledge, snape))