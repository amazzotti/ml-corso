"""Esercizio 6 (Modulo 1) - Indovina il numero (ciclo while).

Teoria: teoria/02_python_avanzato.md, sezioni 3 e 4.

OBIETTIVO
Il programma sceglie un numero casuale tra 1 e 100. L'utente prova a
indovinarlo; a ogni tentativo il programma dice "troppo alto" o
"troppo basso". Quando l'utente indovina, il programma dice in quanti
tentativi ci e' riuscito.

ESEMPIO DI SVOLGIMENTO (numero segreto: 37)
    Indovina il numero tra 1 e 100: 50
    Troppo alto!
    Indovina il numero tra 1 e 100: 25
    Troppo basso!
    Indovina il numero tra 1 e 100: 37
    Bravo! Hai indovinato in 3 tentativi.

CONCETTI NUOVI
- import random e random.randint(1, 100): intero casuale, estremi inclusi.
- while True: ciclo che continua finche' non incontra un break.
- break: esce subito dal ciclo.
- Una variabile contatore che parte da 0 prima del ciclo e aumenta di 1
  a ogni tentativo (come l'accumulatore dell'esercizio sui cicli).
- if / elif / else dentro un ciclo.

STRUTTURA SUGGERITA
    import random
    segreto = random.randint(1, 100)
    tentativi = 0
    while True:
        1. chiedi il numero (ricorda int(...))
        2. aumenta tentativi
        3. se e' uguale al segreto: stampa il messaggio finale e break
        4. altrimenti se e' maggiore: "Troppo alto!"
        5. altrimenti: "Troppo basso!"

COME VERIFICARE DA SOLO
- Per provare senza fare 7 tentativi, scrivi temporaneamente
  segreto = 50 al posto di random.randint(...) e controlla che con 50
  il programma finisca subito dicendo "1 tentativo". Poi rimetti random.
- Un modo furbo di giocare e' la ricerca binaria: provare sempre il
  numero a meta' dell'intervallo. Con 100 numeri bastano al massimo 7
  tentativi. Se ci metti molto di piu', c'e' un errore negli indizi.

ERRORI TIPICI
- Il numero casuale scelto DENTRO il ciclo: cambierebbe a ogni giro.
  Va scelto una volta sola, prima del while.
- Dimenticare il break: il programma non finisce mai (Ctrl+C per fermarlo).
- Confrontare un testo con un numero: serve int() sull'input.

BONUS (facoltativo)
- Limita i tentativi a 7: se finiscono, stampa "Hai perso, il numero era X".
  Suggerimento: puoi mettere la condizione nel while: while tentativi < 7.
- Alla fine chiedi "Vuoi rigiocare? (s/n)" e ripeti il gioco.
- Gestisci il caso in cui l'utente scrive del testo invece di un numero
  (dopo l'esercizio 10 sul try/except, torna qui e sistemalo).
- Chiedi all'inizio il livello (facile 1-50, medio 1-100, difficile 1-1000).

Scrivi il tuo codice qui sotto.
"""

import random
segreto = random.randint(1, 100)
tentativi = 0
while True:
    numero = int(input("Indovina il numero tra 1 e 100: "))
    tentativi += 1
    if numero == segreto:
        print(f"Bravo! Hai indovinato in {tentativi} tentativi.")
        break
    elif numero > segreto:
        print("Troppo alto!")
    else:
        print("Troppo basso!")  