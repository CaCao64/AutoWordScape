from dictionnaire import Dictionnaire

class Niveau:
    def __init__(self, lettres):
        self.lettres = lettres
        self.dictionnaire = Dictionnaire()

    def combinaisons2(self,taille):
        if taille==1:
            return self.lettres
        
        resultats = []
        liste = self.combinaisons2(taille-1)
        for lettre in self.lettres:
            for element in liste:
                if lettre not in element:
                    combinaison = element + lettre
                    resultats.append(combinaison)
        return resultats

    def combinaisons(self):
        resultat = []
        for taille in range(2,len(self.lettres)+1):
            c=self.combinaisons2(taille)
            resultat.extend(c)
        return resultat

    def solutions(self):
        resultat=[]
        combinaisons=self.combinaisons()
        for mot in combinaisons:
            if self.dictionnaire.estDansDictionnaire(mot):
                resultat.append(mot)
        return resultat
