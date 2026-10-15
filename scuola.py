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

    def conta_studenti(self):
        return len(self.studenti)
        
    def elenco_studenti(self):
        return self.studenti

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
    
    def conta_studenti(self):
        return len(self.studenti)
    
    def elenco_studenti(self):
        return self.studenti   

if __name__ == "__main__":
    scuola = Scuola("Istituto Tecnico")

    scuola.aggiungi_studente(Studente("Marco", "Rossi", 16))
    scuola.aggiungi_studente(Studente("Sara", "Neri", 18))
    scuola.aggiungi_studente(Studente("Francesco", "Rossi", 15))
    scuola.aggiungi_studente(Studente("Alessandro", "Bianchi", 16))

    print(f"Numero studenti: {scuola.conta_studenti()}")

    for studente in scuola.cerca_per_cognome("rossi"):
        print(studente)
        print(f"Classificazione: {studente.classificazione()}")

    print("Studenti di 18 anni:")
    for studente in scuola.cerca_per_eta(18):
        print(f"- {studente.nome} {studente.cognome}")

    quinta = Classe("5", "A")
    quinta.aggiungi_studente(scuola.studenti[1])
    print(f"Classe {quinta.anno}{quinta.sezione}: {len(quinta.studenti)} studenti.")

    terza = Classe("3", "A")
    terza.aggiungi_studente(scuola.studenti[0])
    terza.aggiungi_studente(scuola.studenti[3])
    print(f"Classe {terza.anno}{terza.sezione}: {len(terza.studenti)} studenti")
