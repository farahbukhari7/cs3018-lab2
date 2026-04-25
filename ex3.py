import termcolor
from logic import *
# Suspects
alice = Symbol("AliceSuspect")
bob = Symbol("BobSuspect")
carol = Symbol("CarolSuspect")
# Rooms
office = Symbol("office")
garage = Symbol("garage")
basement = Symbol("basement")
# Weapons
poison = Symbol("poison")
rope = Symbol("rope")
candlestick = Symbol("candlestick")
symbols = [alice, bob, carol, office, garage, basement, poison, rope, candlestick]
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    # Layer 1: at least one of each category
    Or(alice, bob, carol),
    Or(office, garage, basement),
    Or(poison, rope, candlestick),
    # Layer 2: cards in YOUR hand (definitely not the answer)
    And(Not(alice), Not(office), Not(poison)),
    # Layer 3: opponent showed you one of these
    Or(Not(bob), Not(garage), Not(rope)),
    # Layer 4: additional cards you learned separately
    Not(candlestick),
    Not(basement)
)
check_knowledge(knowledge)