"""Esercizio 2 (Modulo 1) - La tabellina con il ciclo for.

Obiettivo: il programma chiede un numero e stampa la sua tabellina
da 1 a 10, una riga per ogni moltiplicazione.

Esempio con 7:
    7 x 1 = 7
    7 x 2 = 14
    ...
    7 x 10 = 70

Concetti nuovi:
- Un CICLO ripete un blocco di codice piu' volte.
- range(1, 11) produce i numeri 1, 2, 3, ..., 10 (l'ultimo, 11, e' ESCLUSO).
- Il ciclo for prende uno alla volta i valori e li mette in una variabile:
      for i in range(1, 11):
          print(i)          <- questa riga e' rientrata: e' dentro il ciclo
- Dentro il ciclo puoi usare la variabile i nei calcoli e nelle f-string:
      print(f"{n} x {i} = {n * i}")

Suggerimento: prima fai stampare solo i numeri da 1 a 10 con il ciclo,
poi aggiungi la moltiplicazione.

Bonus (facoltativo):
- Chiedi anche fino a quale numero arrivare (non sempre 10).
- Con un ciclo for, calcola la somma dei numeri da 1 a 100.
  Si fa con una variabile "totale" che parte da 0 e a ogni giro aumenta.
  (Risultato atteso: 5050.)

Scrivi il tuo codice qui sotto.
"""

