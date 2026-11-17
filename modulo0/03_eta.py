"""Esercizio 3 - Nome ed eta' tra 10 anni.

Obiettivo: il programma chiede nome ed eta' e stampa una frase come
"Marco, tra 10 anni avrai 40 anni".

Concetti nuovi:
- input() restituisce sempre TESTO, anche se si scrive 30.
- Per fare calcoli serve convertire il testo in numero intero con int():
      eta = int(input("Quanti anni hai? "))
- Con i numeri si possono usare + - * / (somma, differenza, prodotto, divisione).

Da provare dopo che funziona: togliere int(...) e sommare 10.
Cosa succede? Leggi bene l'errore: e' uno dei piu' comuni per chi inizia.

Suggerimento: per la frase puoi usare una f-string,
    print(f"{nome}, tra 10 anni avrai {eta + 10} anni")

Scrivi il tuo codice qui sotto.
"""
nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))
print(f"{nome}, tra 10 anni avrai {eta + 10} anni")