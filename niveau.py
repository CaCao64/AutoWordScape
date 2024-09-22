class Niveau:
    def __init__(self, lettres):
        self.lettres = lettres
        
    def combinaisons(self,taille):
        if taille==1:
            return self.lettres
        
        resultats = []
        liste = self.combinaisons(taille-1)
        for lettre in self.lettres:
            for element in liste:
                combinaison = element + lettre
                resultats.append(combinaison)
        return resultats
    

