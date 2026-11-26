"""Esercizio 8 (Modulo 1) - Contatore di parole.

Teoria: teoria/02_python_avanzato.md, sezioni 2 e 5; teoria/01_python_base.md, sezione 10.

OBIETTIVO
Dato un testo, contare quante volte compare ogni parola e stampare le
5 piu' frequenti, dalla piu' frequente alla meno frequente.

TESTO DI PROVA
    testo = "Il gatto e il cane e il topo. Il gatto dorme, il cane no!"

RISULTATO ATTESO (la parola e il numero di volte)
    il: 5
    gatto: 2
    cane: 2
    e: 2
    topo: 1
(Le parole con lo stesso conteggio possono comparire in ordine diverso.)

PASSI
1. Porta tutto in minuscolo: "Il" e "il" devono contare come la stessa parola.
   testo.lower()
2. Togli la punteggiatura (. , ! ?): con replace, una volta per ciascun
   simbolo, oppure con un ciclo su una stringa di simboli.
3. Dividi in parole: testo.split()  ->  lista di stringhe.
4. Conta con un dizionario: la chiave e' la parola, il valore e' il conteggio.
   Per ogni parola:
       se e' gia' nel dizionario aumenta il valore di 1,
       altrimenti inizia a 1.
   (Oppure: conteggi[p] = conteggi.get(p, 0) + 1, che fa tutto in una riga.)
5. Ordina le coppie per conteggio decrescente:
       ordinate = sorted(conteggi.items(), key=lambda coppia: coppia[1], reverse=True)
   coppia[1] e' il secondo elemento della coppia (parola, conteggio).
6. Prendi le prime 5 con ordinate[:5] e stampale con un ciclo for.

CONCETTI NUOVI
- Metodi delle stringhe: lower, replace, split.
- Dizionario usato come CONTATORE.
- sorted con key e reverse; lambda (funzione scritta su una riga).
- Slicing di una lista: lista[:5] = primi 5 elementi.

COME VERIFICARE DA SOLO
- Il totale dei conteggi deve essere uguale a len(testo.split()).
  Per il testo di prova: 14 parole in tutto.
      assert sum(conteggi.values()) == 14
- Il numero di parole DIVERSE e' len(conteggi): per il testo di prova, 7
  (il, gatto, e, cane, topo, dorme, no).

ERRORI TIPICI
- Non togliere la punteggiatura: "topo." e "topo" risultano parole diverse.
- Dimenticare lower(): "Il" e "il" contate separatamente.
- sorted(conteggi) ordina solo le chiavi (alfabeticamente), non i conteggi.
  Serve .items() e key=.

BONUS (facoltativo)
- Metti il testo in un file e leggilo (dopo l'esercizio 9 sui file).
- Ignora le parole molto comuni ("il", "e", "di", ...) con una lista di
  parole da escludere.
- Trova la parola piu' lunga e la lunghezza media delle parole.
- Metti tutto in una funzione conta_parole(testo) che RESTITUISCE il
  dizionario, e scrivi un assert sul testo di prova.

Scrivi il tuo codice qui sotto.
"""
testo = "Il gatto e il cane e il topo. Il gatto dorme, il cane no!"
testo = testo.lower()
testo = testo.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
parole = testo.split()
conteggi = {}
for p in parole:
    conteggi[p] = conteggi.get(p, 0) + 1
ordinate = sorted(conteggi.items(), key=lambda coppia: coppia[1], reverse=True)
for parola, conteggio in ordinate[:5]:
    print(f"{parola}: {conteggio}")
