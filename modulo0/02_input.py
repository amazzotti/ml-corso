"""Esercizio 2 - Chiedere il nome e salutare.

Obiettivo: il programma chiede il nome all'utente e poi lo saluta,
per esempio con "Ciao, Marco!".

Concetti nuovi:
- input("Come ti chiami? ") mostra la domanda, aspetta che l'utente scriva
  e restituisce quello che e' stato scritto.
- Una variabile e' un nome a cui si assegna un valore: nome = "Marco".
  Poi si puo' usare dentro print.

Per unire testo fisso e variabile:
- print("Ciao,", nome)
- oppure una f-string: print(f"Ciao, {nome}!")
"""

nome = input("Come ti chiami? ")
print("Ciao,", nome)
