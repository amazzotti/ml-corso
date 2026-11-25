"""Esercizio 4 (Modulo 1) - I dizionari: una piccola rubrica.

Obiettivo: il programma gestisce una rubrica nome -> numero di telefono.
Parte con 3 contatti gia' scritti nel codice, poi chiede un nome:
- se il nome c'e', stampa il numero;
- se non c'e', dice che il contatto non esiste.
Infine permette di aggiungere un nuovo contatto e stampa tutta la rubrica.

Esempio:
    Che nome cerchi? Anna
    Anna: 333111222
    Nome del nuovo contatto: Luca
    Numero: 340555666
    Rubrica completa:
    Anna: 333111222
    ...
    Luca: 340555666

Concetti nuovi:
- Un DIZIONARIO associa una CHIAVE a un VALORE, tra parentesi graffe:
      rubrica = {"Anna": "333111222", "Marco": "347000111"}
- Leggere un valore dalla chiave:
      rubrica["Anna"]            <- da' "333111222" (errore se non esiste)
- Aggiungere o cambiare un elemento:
      rubrica["Luca"] = "340555666"
- Controllare se una chiave esiste:
      if "Anna" in rubrica:
          ...
- Scorrere chiave e valore insieme:
      for nome, numero in rubrica.items():
          print(nome, numero)

Le liste si leggono per POSIZIONE (voti[0]); i dizionari per CHIAVE.
Quando conviene l'uno e quando l'altro? Pensaci mentre scrivi.

Suggerimento: usa "in" per controllare che il nome esista PRIMA di
leggerlo, cosi' non ottieni un errore (KeyError).

Bonus (facoltativo):
- Il numero di telefono lo tratti come testo (str). Perche' non come
  numero intero? Pensa a cosa succede con lo zero iniziale.
- Con rubrica.get("Nome", "non trovato") ottieni un valore di riserva
  senza usare l'if. Prova a riscrivere la ricerca cosi'.
- Stampa quanti contatti ci sono con len(rubrica).

Scrivi il tuo codice qui sotto.
"""

rubrica = {"Anna": "333111222", "Marco": "347000111", "Ale": "320222333"}
nome = input("Che nome cerchi? ")
if nome in rubrica:
      print(nome, rubrica[nome])
else:
      print("Contatto non esistente")
print("Nome del nuovo contatto: ")
nuovo_nome = input()
print("Numero: ")
nuovo_numero = input()
rubrica[nuovo_nome] = nuovo_numero
print("Rubrica completa:")
for nome, numero in rubrica.items():
      print(nome, numero)