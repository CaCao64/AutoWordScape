class Dictionnaire:
    fileName = "ods6.txt"
    folder = "dictionnaire"
    def __init__(self):
        self.dictionnaire = {}
        path = Dictionnaire.folder + "\\" + Dictionnaire.fileName
        file  = open(path,"r",encoding="utf8")
        lines = file.readlines()
        for line in lines:
            line=line.strip()
            # print(f"Ligne {line}")
            self.dictionnaire[line] = True
        file.close()

    def estDansDictionnaire(self,mot):
        return mot in self.dictionnaire
