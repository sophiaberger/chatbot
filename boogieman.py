__author__ = 'sophia'

import random
def howdy():
    n = str(raw_input())
    if n != "":
        l = ["Hello!", "Hi!", "Yo Gabba Gabba!", "You're an awful person."]
        x = random.randrange(0,4)
        print(l[x])
        return x
    if n == "":
        n = str(raw_input("Say whuh?! "))
        howdy()

def insulted():
    n = str(raw_input())
    if n != "":
        l = ["Jk.", "You are!", "You are,", "Hey, dude, shut up."]
        x = random.randrange(0,4)
        print(l[x])
    if n == "":
        insulted()

while True:
    p = howdy()
    if p == 3:
        insulted()


