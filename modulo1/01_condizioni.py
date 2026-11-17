"""Esercizio 1 (Modulo 1) - Positivo, negativo o zero.

Obiettivo: il programma chiede un numero e stampa se e' positivo,
negativo oppure zero.

Esempi:
    5   ->  "5.0 e' positivo"
    -3  ->  "-3.0 e' negativo"
    0   ->  "0.0 e' zero"

Concetti nuovi:
- Un CONFRONTO da' come risultato True (vero) o False (falso):
      >   maggiore        <   minore
      >=  maggiore o uguale   <=  minore o uguale
      ==  uguale (attenzione: DUE uguali; uno solo e' l'assegnazione)
      !=  diverso
- if / elif / else: il programma sceglie quale blocco eseguire.
      if condizione1:
          ...        <- eseguito se condizione1 e' vera
      elif condizione2:
          ...        <- altrimenti, se condizione2 e' vera
      else:
          ...        <- in tutti gli altri casi
- INDENTAZIONE: le righe dentro un blocco vanno rientrate di 4 spazi
  (VS Code lo fa con il tasto Tab). In Python l'indentazione fa parte
  del codice: senza, il programma non parte.
- I due punti ":" alla fine di if / elif / else sono obbligatori.

Suggerimento: l'ordine dei controlli conta. Pensa a quali casi
devi distinguere e quanti rami ti servono.

Bonus (facoltativo): chiedi anche l'eta' e stampa "maggiorenne" o
"minorenne". Poi prova a scrivere "ciao" invece di un numero:
cosa succede? (Ci torneremo con try/except.)

Scrivi il tuo codice qui sotto.
"""

numero = float(input("Inserisci un numero: "))
if numero > 0:
    print(f"{numero} e' positivo")
elif numero < 0:
    print(f"{numero} e' negativo")
else:
    print(f"{numero} e' zero")

eta = int(input("Inserisci età: "))
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")