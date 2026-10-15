class Studente:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def classificazione(self):
        if self.eta < 16:
            return "Biennio"
        else:
            return "Triennio"

    def __str__(self):
        return f"Nome: {self.nome}. Cognome: {self.cognome}. Età: {self.eta}"

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
