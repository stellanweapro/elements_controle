#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:50:47 2020

@author: stellanwea
"""


import numpy as np 
choix_niveau = input(str('Voulez-vous effectuer un pari facile, moyen ou risqué ? : '))
niveau = {'facile' : 1.3,
          'moyen' : 1.8,
          'risqué' : 2.5}
l = np.arange(1,4)

def mise_total(humeur) :
    a = np.random.randint(1,len(humeur)+1,1)
    if a == 1 :
        return 10
    elif a == 2:
        return 20
    else : 
        return 50
    
mise = mise_total(l)

print(f"\nLe joueur retire {mise} euros pour jouer sur une côte {choix_niveau} donc une côte à {niveau[choix_niveau]} \n")

def seuil_limit() :
    s = np.random.rand(1)
    print(f"Le seuil est {s**-1}\n")
    return s

def choix_type_jeu(niveau, mise,seuil) :
    for i in niveau.values() :
        if (1/i) > seuil :
            print(f"Le jeu est gagnant, le gain est {(mise * i)-mise} en ayant parié {mise} \n")
            return (mise*i)
        else :
            print(f"Le jeu est perdant, le joueur perd sa mise \n")
            return 0

jeu = True
while jeu == True :
    partie = 1
    seuil = seuil_limit()
    res = choix_type_jeu(niveau, mise,seuil)
    mise = res
    print(f"Finalement, le joueur finit le jeu avec {res} euros \n")
    partie += 1
    if res == 0 :
        print(f"Le joueur a perdu toute sa mise au bout de {partie} partie(s) \n\n")
        jeu = False


