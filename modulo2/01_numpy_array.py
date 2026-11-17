"""Esercizio 1 (Modulo 2) - Primi array con NumPy.

Prima di iniziare:  pip install numpy pandas matplotlib   (ambiente .venv attivo)
Teoria: teoria/03_numpy_pandas.md, sezioni 2, 3 e 5.

OBIETTIVO
Creare array, leggerne le proprieta' e calcolare le statistiche di base.

PASSI
1. Importa NumPy:  import numpy as np
2. Crea  a = np.array([4, 8, 15, 16, 23, 42])  e stampa:
   shape, ndim, size, dtype.
3. Calcola e stampa: somma, media, minimo, massimo, mediana, deviazione
   standard, e la POSIZIONE del massimo (argmax).
4. Crea altri array con:  np.zeros(4),  np.ones((2, 3)),
   np.arange(0, 10, 2),  np.linspace(0, 1, 5)  e stampali. Osserva:
   arange ESCLUDE l'ultimo valore, linspace lo INCLUDE.
5. Slicing sull'array a:  a[0],  a[-1],  a[1:4],  a[::2].
6. Genera 1000 numeri casuali con un seed fisso:
       rng = np.random.default_rng(42)
       x = rng.normal(170, 10, 1000)
   (media 170, deviazione standard 10) e stampa media e deviazione
   standard di x. Cambia il seed e osserva che i numeri cambiano; rimetti
   42 e osserva che tornano uguali (ripetibilita').

RISULTATI ATTESI per a = [4, 8, 15, 16, 23, 42]
    shape (6,)   ndim 1   size 6   dtype int64 (su alcune versioni int32)
    somma 108    media 18.0   mediana 15.5   min 4   max 42   argmax 5
    deviazione standard circa 12.32
    a[1:4]  ->  [ 8 15 16]      a[::2]  ->  [ 4 15 23]
Per x: media vicina a 170 (169-171) e deviazione standard vicina a 10.

CONCETTI NUOVI
- array: tutti gli elementi dello stesso tipo (dtype).
- shape = forma; (6,) significa vettore con 6 elementi.
- arange (fine escluso) contro linspace (estremi inclusi, numero di punti).
- slicing: a[inizio:fine:passo], fine escluso.
- seed e default_rng: numeri casuali ripetibili.
- np.median, a.std(), a.argmax().

COME VERIFICARE DA SOLO
    assert a.sum() == 108
    assert a.mean() == 18
    assert np.median(a) == 15.5
    assert abs(a.std() - 12.3153) < 1e-3
    assert a.argmax() == 5
    assert list(a[1:4]) == [8, 15, 16]
    assert len(np.linspace(0, 1, 5)) == 5 and np.linspace(0, 1, 5)[-1] == 1
    assert len(np.arange(0, 10, 2)) == 5 and np.arange(0, 10, 2)[-1] == 8

ERRORI TIPICI
- Dimenticare "import numpy as np" (NameError: name 'np' is not defined).
- Confondere argmax (la posizione) con max (il valore).
- Aspettarsi che arange(0, 10, 2) arrivi a 10.
- Usare le liste e stupirsi: [1, 2] * 2 e' [1, 2, 1, 2]; np.array([1, 2]) * 2
  e' [2 4]. Prova la differenza.

BONUS (facoltativo)
- Confronta media e mediana di np.array([1, 2, 3, 100]): perche' sono tanto
  diverse? (Vedi la sezione sulla statistica.)
- Calcola il coefficiente di variazione: std / mean.
- Normalizza a: (a - media) / std. Quanto vale la media del risultato?
  (Circa 0.) E la deviazione standard? (1.)

Scrivi il tuo codice qui sotto.
"""

