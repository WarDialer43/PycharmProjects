from random import choice

Emperium_of_man = "known univers"
Master_of_mankind = "The Emperor"
Primarks = "Son of the Emperor of mankind"
Legion_Astartes = "Space Marines Chapters"


def random_facts():
    facts = [
        "The emperium of man is vast and incompasses most of the known galaxies.",
        "The Emperor is the most powerful psyker to ever walk the earth and has been around for centuries."
        "The Primarks were gemetically crafted by the Emperor to lead his armies in a crusade."
        "The Legion Astartes is made up of 20 Chapters lead by a Primark."
    ]

    index = choice("0123")

    print(facts[int(index)])


if __name__ == "__main__":
    random_facts()




