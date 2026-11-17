"""Esercizio 7 (Modulo 1) - FizzBuzz.

Teoria: teoria/01_python_base.md, sezioni 6, 7 e 8.

OBIETTIVO
Per ogni numero da 1 a 100 stampa:
- "FizzBuzz" se e' multiplo di 3 E di 5;
- "Fizz" se e' multiplo di 3;
- "Buzz" se e' multiplo di 5;
- altrimenti il numero stesso.

PRIME RIGHE ATTESE
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    ...

CONCETTI
- Un numero e' multiplo di k quando il resto della divisione per k e' 0:
      n % 3 == 0
- Condizioni combinate: if n % 3 == 0 and n % 5 == 0:
- L'ORDINE dei controlli e' decisivo: Python si ferma al primo ramo vero.
  Se controlli "multiplo di 3" per primo, il 15 stampa "Fizz" e non
  "FizzBuzz". Pensa a quale caso deve venire prima.
- Un numero multiplo di 3 e di 5 e' multiplo di 15.

COME VERIFICARE DA SOLO
Invece di stampare, conta quante volte compare ogni caso (con tre
variabili contatore, come negli esercizi sui cicli) e controlla:
    "FizzBuzz": 6    (15, 30, 45, 60, 75, 90)
    "Fizz":     27   (i multipli di 3 non multipli di 5)
    "Buzz":     14   (i multipli di 5 non multipli di 3)
    numeri normali: 53
La somma deve fare 100.

ERRORI TIPICI
- Controlli nell'ordine sbagliato (il 15 stampa Fizz).
- Usare "if" al posto di "elif" per tutti i rami: il 15 stamperebbe
  piu' righe. Rifletti sulla differenza tra una catena if/elif e piu'
  if separati.
- range(1, 100) si ferma a 99: per arrivare a 100 serve range(1, 101).

BONUS (facoltativo)
- Rendi parametrici i numeri: chiedi all'utente i due divisori (3 e 5)
  e il limite.
- Scrivi una funzione fizzbuzz(n) che RESTITUISCE la stringa corretta per
  un numero, poi usala in un ciclo. Verificala con assert:
      assert fizzbuzz(15) == "FizzBuzz"
      assert fizzbuzz(9) == "Fizz"
      assert fizzbuzz(10) == "Buzz"
      assert fizzbuzz(7) == "7"
- Stampa i risultati su una sola riga separati da virgole, usando
  ", ".join(lista_di_stringhe).

Scrivi il tuo codice qui sotto.
"""

