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
