#!/usr/bin/python3
"""
Contains dummy data to use for creating the database
and the randomizer function.
"""
import random

usernames = [
    "Leodickaprio",
    "Buttpit",
    "Indianodolys",
    "Sexrogen",
    "barrackbomer"]

passwords = ["iluvd", "ussucks", "whichhole?", "Ineedwipes", "allahwakbar"]

tags = ["violent", "funny", "wholesome", "cringe", "wtf"]

posts = [
    "Never let your best friends get lonely, keep disturbing them.",
    "If Cinderella’s shoe fit perfectly, then why did it fall off?",
    "Papercut: A tree’s final moment of revenge.",
    "When nothing is going right, go left.",
    "My six pack is protected by a layer of fat.",
    "I could agree with you, but then we’d both be wrong.",
    "Lottery: a tax on people who are bad at math.",
    "My windows aren’t dirty, my dog is painting.",
    "I love my job only when I’m on vacation.",
    "I am on a seafood diet. I see food, and I eat it.",
    "If Monday had a face, I would punch it.",
    "A balanced diet means a cupcake in each hand."
]


def randM(random_list):
    """Returns a random item from a list"""
    return random.choice(random_list)
