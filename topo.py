# on peut ajouter des listes

l1 = [1, 2]
l2 = [5]

l3 = l1 + l2
l4 = [*l1, *l2]
l5 = []
for l in [l1, l2]:
    for element in l:
        l5.append(element)

print(l3 == l4 == l5 == [1, 2, 5])

# penser a creer si besoin une variable res qui contiendra le resultat


def mafonction_de_filtrage(uneliste):
    res = []
    # votre code
    return res


def autre_fonction(quelquechose):
    res = {}
    # votre code
    return res


def unecontiondeformattage(a):
    return f"le premier paramètre vaut {a}"


# renvoyer plusieurs valeurs


def minmax(liste):
    min_ = min(liste)
    max_ = max(liste)
    return min_, max_  # attention cela renvoie un tuple.


def minmax2(liste):
    return min(liste), max(liste)


def minmax3(liste):
    min_ = min(liste)
    return (min_, max(liste))


l = [5, 2, 3, 7, 9, 8]

print(minmax(l) == minmax2(l) == minmax3(l) == (2, 9))

print("Z".lower() == "z" == "Z".lower())

for l in "Exemple":
    print(l, l.lower(), l.upper())

# Je n'aime pas son exemple qui laisse croire qu'une methode ne peut faire qu'afficher des choses.


class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def sit(self):
        return f"{self.owner}'s dog is called ({self.name}) and is sitting"

    def eat(self, food):
        return f"{self.name} is eating {food}"


unchien = Dog("rintintin", "toto")
print(unchien.sit())
if unchien.name == "rintintin":
    print("Oh mais c'est rintintin !" )
print(unchien.eat("paté"))

# Bien connaitre ses gammes sur les parvous de structures de données et les listes en compréhension
