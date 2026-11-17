"""Esercizio 3 (Modulo 1) - Le liste: voti e media.

Obiettivo: il programma chiede 5 voti, li salva in una lista e poi stampa
il voto piu' alto, quello piu' basso e la media.

Esempio con i voti 6, 8, 7, 9, 5:
    Voti: [6.0, 8.0, 7.0, 9.0, 5.0]
    Massimo: 9.0
    Minimo: 5.0
    Media: 7.0

Concetti nuovi:
- Una LISTA contiene piu' valori in ordine, tra parentesi quadre:
      voti = [6, 8, 7]
      voti = []                 <- lista vuota
- Aggiungere un elemento in fondo:
      voti.append(9)
- Leggere un elemento per posizione (si parte da 0!):
      voti[0]    <- il primo
      voti[-1]   <- l'ultimo
- Quanti elementi ci sono:
      len(voti)
- Funzioni pronte per le liste di numeri:
      max(voti)   min(voti)   sum(voti)
- Si puo' scorrere una lista con il for:
      for v in voti:
          print(v)

Suggerimento: parti da una lista vuota, poi con un ciclo for che gira
5 volte chiedi un voto con input() e lo aggiungi con append().
La media e' sum(voti) / len(voti).

Bonus (facoltativo):
- Fai stampare la lista ordinata: sorted(voti).
- Conta quanti voti sono sufficienti (>= 6) con un ciclo e una
  variabile contatore, come il "totale" dell'esercizio precedente.
- Chiedi all'inizio quanti voti inserire, invece di fissare 5.

Scrivi il tuo codice qui sotto.
"""

