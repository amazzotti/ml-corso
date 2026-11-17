"""Esercizio 5 (Modulo 3) - Il gradiente scritto con la formula.

Teoria: teoria/04_regressione_gradient_descent.md, sezione 6.

OBIETTIVO
Scrivere le derivate della perdita rispetto a w e b con la formula esatta
(analitica) e verificarle contro la derivata numerica dell'esercizio 4.

LE FORMULE (derivazione completa nella teoria)
Con  e_i = w * x_i + b - y_i  (errore del campione i):
       dL/dw = (2 / N) * somma( e_i * x_i )
       dL/db = (2 / N) * somma( e_i )
In NumPy:  dw = 2 * np.mean(e * x)    db = 2 * np.mean(e)

PASSI
1. Scrivi la funzione:
       def gradiente(x, y, w, b):
           e = w * x + b - y
           dw = 2 * np.mean(e * x)
           db = 2 * np.mean(e)
           return dw, db
2. Prova prima su un esempio MINUSCOLO, da verificare a mano:
       xs = np.array([1.0, 2.0, 3.0])
       ys = np.array([2.0, 4.0, 6.0])
       gradiente(xs, ys, 0, 0)    ->  (-18.667, -8.0)
   Calcolo a mano: e = [-2, -4, -6];
       dw = (2/3) * (-2*1 + -4*2 + -6*3) = (2/3) * (-28) = -18.667
       db = (2/3) * (-2 - 4 - 6)         = (2/3) * (-12) = -8.0
3. Calcola il gradiente sui 50 dati (seed 42) nei punti:
       (0, 0)  ->  (-153.77, -22.91)
       (2, 1)  ->  (   2.40,   0.50)
   Sono gli stessi numeri trovati con la derivata numerica nell'esercizio 4.
4. Scrivi gradiente_numerico(x, y, w, b, eps=1e-5) che usa la derivata numerica
   (come nell'esercizio 4) e confronta con quello analitico in 5 punti scelti
   a caso (w, b tra -5 e 5, con rng.uniform):
       assert np.allclose(analitico, numerico, atol=1e-3)

CONCETTI NUOVI
- Derivata analitica con la REGOLA DELLA CATENA: la funzione esterna e'
  il quadrato (derivata 2e), la interna e' l'errore (derivata x rispetto a w,
  1 rispetto a b).
- Gradient check: confrontare il gradiente analitico con quello numerico e'
  IL modo per scoprire errori nelle formule.
- Il gradiente e' un vettore (dw, db): una derivata per parametro.

COME VERIFICARE DA SOLO
    dw, db = gradiente(xs, ys, 0, 0)
    assert abs(dw + 18.6667) < 1e-3 and abs(db + 8.0) < 1e-9
    dw, db = gradiente(x, y, 0, 0)
    assert abs(dw + 153.77) < 0.01 and abs(db + 22.91) < 0.01
    dw, db = gradiente(x, y, 2, 1)
    assert abs(dw - 2.40) < 0.01 and abs(db - 0.50) < 0.01

ERRORI TIPICI
- Dimenticare il fattore 2 (il gradiente risulta meta' del vero).
- Dimenticare "* x" nel gradiente di w (le due componenti diventano uguali).
- Segno invertito degli errori (y - y_pred invece di y_pred - y): il gradiente
  cambia segno e il gradient descent andrebbe in salita.
- Usare np.sum al posto di np.mean senza dividere per N.

BONUS (facoltativo)
- Verifica che nel punto della soluzione esatta (w, b) = np.polyfit(x, y, 1) il
  gradiente sia (circa) zero: nel fondo della valle la pendenza e' nulla.
- Scrivi la versione per piu' feature (X di forma (N, d)) della teoria,
  sezione 10:  dw = 2 * X.T @ e / N  e controlla le forme.
- Disegna il gradiente come freccia su un grafico dei dati: in che direzione
  dovrebbe muoversi la retta?

Scrivi il tuo codice qui sotto.
"""

