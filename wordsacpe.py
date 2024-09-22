from niveau import Niveau

n = Niveau(["R","P","A","C"])
combinaisons=n.combinaisons(4)
print("Taille : "+str(len(combinaisons)))
print(combinaisons)
