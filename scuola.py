class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def cerca_per_cognome(self, cognome):
        cognome = cognome.lower()
        return [studente for studente in self.studenti if studente.cognome.lower() == cognome]
    
    def cerca_per_eta(self, eta):
        return [studente for studente in self.studenti if studente.eta == eta]
    
    def conta_studenti_scuola(self):
        return len(self.studenti)
    
    def elenco_studenti_scuola(self):
        return self.studenti   
