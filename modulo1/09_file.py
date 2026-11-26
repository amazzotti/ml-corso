r"""Esercizio 9 (Modulo 1) - Leggere e scrivere file.

Teoria: teoria/02_python_avanzato.md, sezione 7.

OBIETTIVO
Un programma che salva dei voti in un file di testo e, in una seconda
parte, li rilegge dal file e calcola la media. Cosi' i dati restano
anche dopo la chiusura del programma.

PARTE A - SCRITTURA
1. Chiedi all'utente 4 voti (con un ciclo for).
2. Scrivili nel file "voti.txt", UNO PER RIGA, nella stessa cartella del
   programma. Esempio del contenuto del file con i voti 6, 8, 7.5, 9:
       6.0
       8.0
       7.5
       9.0
   (Ogni riga termina con "\n": write non lo aggiunge da solo.)

PARTE B - LETTURA
3. Apri "voti.txt" in lettura, leggi tutte le righe, togli gli a-capo con
   strip(), converti ogni riga in float e mettile in una lista.
4. Stampa la lista e la media.

PARTE C - AGGIUNGERE
5. Chiedi un ulteriore voto e AGGIUNGILO in fondo al file senza cancellare
   gli altri (modalita' "a"). Poi rileggi e ristampa la media.

STRUTTURA SUGGERITA
    from pathlib import Path
    percorso = Path(__file__).parent / "voti.txt"

    with open(percorso, "w", encoding="utf-8") as f:
        f.write(f"{voto}\n")           # dentro il ciclo

    with open(percorso, "r", encoding="utf-8") as f:
        righe = f.readlines()
    voti = [float(r.strip()) for r in righe]

CONCETTI NUOVI
- open(percorso, modo): modi "r" lettura, "w" scrittura (cancella il file),
  "a" aggiunta in fondo.
- with ... as f: chiude il file da solo, anche se c'e' un errore.
- write non va a capo: bisogna scrivere "\n".
- readlines() restituisce una lista di righe (con "\n" finale).
- Path(__file__).parent: la cartella dove si trova questo file; cosi' il
  programma funziona da qualunque cartella lo lanci e su qualsiasi PC.
- Comprehension: [float(r.strip()) for r in righe] = ciclo che costruisce
  una lista, in una riga.

COME VERIFICARE DA SOLO
- Dopo la Parte A apri voti.txt da VS Code: devi vedere un voto per riga.
- Con i voti 6, 8, 7.5, 9 la media deve essere 7.625.
- Con l'aggiunta del voto 10 la media diventa 8.1 (40.5 / 5).
- Rilancia il programma due volte: la Parte A con "w" ricomincia da zero
  (il file viene sovrascritto), con "a" invece i voti si accumulano.
  Osserva la differenza.

ERRORI TIPICI
- Dimenticare "\n": tutti i voti finiscono sulla stessa riga ("68.57.59.0").
- float("6.0\n") funziona, ma e' bene usare strip() comunque; con una riga
  vuota finale invece float("") da' ValueError.
- Usare "w" quando si voleva aggiungere: il file viene svuotato.
- Scrivere un percorso assoluto tipo C:\Users\... : non funzionerebbe su
  un altro PC. Usa Path(__file__).parent.
- Lasciare il file voti.txt nel repository: e' un file generato, non va
  pubblicato (verra' ignorato).

BONUS (facoltativo)
- Se il file non esiste ancora, la lettura da' FileNotFoundError: dopo
  l'esercizio 10 gestiscilo con try/except.
- Salva anche il nome della materia nella stessa riga, separato da una
  virgola: "matematica,7.5". In lettura usa split(",").
- Conta quante righe ha il file e stampa il voto massimo e minimo.

Scrivi il tuo codice qui sotto.
"""
from pathlib import Path
percorso = Path(__file__).parent / "voti.txt"
voti = []
for _ in range(4):
    voto = float(input("Inserisci un voto: "))
    voti.append(voto)

with open(percorso, "w", encoding="utf-8") as f:
    for voto in voti:
        f.write(f"{voto}\n")

with open(percorso, "r", encoding="utf-8") as f:
  righe = f.readlines()
voti = [float(r.strip()) for r in righe]
print(f"Voti: {voti}")
print(f"Media: {sum(voti) / len(voti)}")

# Aggiungere un quinto voto senza cancellare gli altri.
voto = float(input("Inserisci un quinto voto: "))

with open(percorso, "a", encoding="utf-8") as f:
    f.write(f"{voto}\n")

with open(percorso, "r", encoding="utf-8") as f:
    righe = f.readlines()
voti = [float(r.strip()) for r in righe]
print(f"Voti: {voti}")
print(f"Media: {sum(voti) / len(voti)}")

