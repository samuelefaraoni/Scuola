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
