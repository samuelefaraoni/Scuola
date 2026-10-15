class Classe:
    def __init__(self, anno, sezione):
        self.anno = anno
        self.sezione = sezione
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def conta_studenti_classe(self):
        return len(self.studenti)
        
    def elenco_studenti_classe(self):
        return self.studenti
