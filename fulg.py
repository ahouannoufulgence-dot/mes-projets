nb_site=int(input("combien de site tu vend par mois ?:"))
prix_unit=int(input("combien vend tu l'unité"))
montant_mensuelle=nb_site*prix_unit
print("votre montant mensuelle est de",montant_mensuelle )
if montant_mensuelle>=5000000: 
    print("le mois a été bien concluant")
else:
    print("ce n'est pas encore concluant,il vous faut redoublé d'effort le mois prochain.")  