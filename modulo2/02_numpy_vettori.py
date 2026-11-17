"""Esercizio 2 (Modulo 2) - Operazioni vettoriali, maschere e velocita'.

Teoria: teoria/03_numpy_pandas.md, sezione 3.

OBIETTIVO
Calcolare su interi array senza cicli for, filtrare con condizioni e
misurare quanto NumPy e' piu' veloce di un ciclo Python.

PARTE A - OPERAZIONI ELEMENTO PER ELEMENTO
    a = np.arange(1, 6)               # [1 2 3 4 5]
    b = np.array([10, 20, 30, 40, 50])
Calcola e stampa (senza for):
    a * 2        ->  [ 2  4  6  8 10]
    a ** 2       ->  [ 1  4  9 16 25]
    a + b        ->  [11 22 33 44 55]
    a * b        ->  [ 10  40  90 160 250]
    np.sqrt(a)   ->  [1. 1.414... 1.732... 2. 2.236...]
Nota: a * b NON e' un prodotto matriciale, e' elemento per elemento.

PARTE B - MASCHERE
    v = np.array([4, 8, 15, 16, 23, 42])
1. Stampa v > 10          ->  [False False  True  True  True  True]
2. Stampa v[v > 10]       ->  [15 16 23 42]
3. Stampa i valori tra 10 e 30 esclusi gli estremi: servono le parentesi e
   l'operatore &:  v[(v > 10) & (v < 30)]   ->  [15 16 23]
4. Conta quanti valori sono pari:  np.sum(v % 2 == 0)   ->  4
   (True vale 1, quindi la somma conta i True.)
5. Sostituisci con 0 tutti i valori maggiori di 20:
       w = v.copy()
       w[w > 20] = 0          ->  [ 4  8 15 16  0  0]

PARTE C - CICLO CONTRO VETTORIALE
Calcola la somma dei quadrati dei numeri da 1 a 1.000.000 in due modi:
1. con un ciclo for e un accumulatore (come nell'esercizio sui cicli);
2. con NumPy, in una riga:
       n = np.arange(1, 1_000_001, dtype=np.int64)
       np.sum(n ** 2)
Misura il tempo di entrambi con il modulo time:
       import time
       inizio = time.perf_counter()
       ... calcolo ...
       durata = time.perf_counter() - inizio
Stampa i due tempi e quante volte NumPy e' piu' veloce.

RISULTATO ATTESO PER LA PARTE C
Il valore e' lo stesso in entrambi i casi: 333333833333500000.
NumPy e' tipicamente da 30 a 200 volte piu' veloce del ciclo (dipende dal PC).

CONCETTI NUOVI
- Vettorializzazione: l'operazione si applica a tutto l'array; il ciclo
  avviene dentro NumPy, in codice compilato.
- Maschere booleane: condizione -> array di True/False -> filtro.
- & (e), | (o), ~ (non) al posto di and/or/not, con le parentesi.
- .copy(): senza, w e v sarebbero lo STESSO array e modificare w
  cambierebbe anche v.
- dtype=np.int64: evita l'overflow su Windows con numeri grandi
  (con int32 il risultato sarebbe sbagliato, senza nessun errore).

COME VERIFICARE DA SOLO
    assert list(a * 2) == [2, 4, 6, 8, 10]
    assert list(a + b) == [11, 22, 33, 44, 55]
    assert list(v[v > 10]) == [15, 16, 23, 42]
    assert list(v[(v > 10) & (v < 30)]) == [15, 16, 23]
    assert np.sum(v % 2 == 0) == 4
    assert list(w) == [4, 8, 15, 16, 0, 0] and v[4] == 23   # v non modificato
    assert totale_numpy == totale_ciclo == 333333833333500000

ERRORI TIPICI
- Usare "and" tra array: ValueError "truth value of an array is ambiguous".
  Serve &, con le parentesi attorno a ogni confronto.
- Dimenticare .copy() e modificare l'array originale senza accorgersene.
- Non specificare dtype=np.int64 e ottenere un numero negativo o strano.
- Cronometrare anche la creazione dell'array: misura solo il calcolo.

BONUS (facoltativo)
- Calcola la distanza euclidea tra due vettori: np.sqrt(np.sum((p - q) ** 2)).
  Per p = [0, 0] e q = [3, 4] deve dare 5.
- Calcola la media mobile su 3 elementi di v senza cicli
  (suggerimento: somma di tre slice sfalsati divisa per 3).
- Prova np.where(v > 20, "alto", "basso").

Scrivi il tuo codice qui sotto.
"""

