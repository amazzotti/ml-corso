"""Esercizio 6 (Modulo 3) - Un passo di gradient descent.

Teoria: teoria/04_regressione_gradient_descent.md, sezione 7.

OBIETTIVO
Fare UN solo passo di discesa del gradiente e verificare che la perdita
scenda. E' il mattone che ripeteremo nel prossimo esercizio.

LA REGOLA
       w  <-  w - lr * dL/dw
       b  <-  b - lr * dL/db
lr (learning rate) e' la lunghezza del passo. Il segno MENO e' fondamentale:
il gradiente indica la salita, noi vogliamo scendere.

PARTE A - ESEMPIO MINUSCOLO (da verificare a mano)
    xs = np.array([1.0, 2.0, 3.0])
    ys = np.array([2.0, 4.0, 6.0])
    w, b, lr = 0.0, 0.0, 0.1
1. Calcola la perdita iniziale (mse) ->  18.667
2. Calcola il gradiente ->  (-18.667, -8.0)
3. Aggiorna:  w = 0 - 0.1 * (-18.667) = 1.867      b = 0 - 0.1 * (-8.0) = 0.8
4. Ricalcola la perdita ->  0.296
   La perdita e' scesa da 18.667 a 0.296 con UN passo.
5. Fai un secondo passo: w = 1.671, b = 0.693, perdita 0.073.
   Annota in un commento cosa osservi: la perdita scende ancora, ma meno.

PARTE B - DATI REALI (50 punti, seed 42)
Riusa predici, mse e gradiente degli esercizi precedenti.
    w, b, lr = 0.0, 0.0, 0.01
1. perdita prima del passo:   163.94
2. gradiente:                 (-153.77, -22.91)
3. dopo il passo:             w = 1.5377    b = 0.2291
4. perdita dopo il passo:     12.04
   Da 163.94 a 12.04 in un passo solo!

PARTE C - L'EFFETTO DEL SEGNO (esperimento)
Rifai la parte B usando per sbaglio il segno PIU': w = w + lr * dw.
Osserva che la perdita SALE (da 163.94 a circa 495). Scrivi in un commento
cosa ti dice questo sul significato del gradiente.

CONCETTI NUOVI
- Discesa del gradiente: piccoli passi nella direzione OPPOSTA al gradiente.
- Learning rate (lr): iperparametro, scelto da noi, non imparato.
- Un passo riduce la perdita (se lr non e' troppo grande).
- Il gradiente e' grande lontano dal minimo e piccolo vicino: i passi si accorciano da soli.

COME VERIFICARE DA SOLO
    # parte A
    assert abs(w1 - 1.8667) < 1e-3 and abs(b1 - 0.8) < 1e-9
    assert abs(perdita_dopo_A - 0.2963) < 1e-3
    # parte B
    assert abs(w - 1.5377) < 1e-3 and abs(b - 0.2291) < 1e-3
    assert abs(perdita_dopo_B - 12.04) < 0.01
    assert perdita_dopo_B < perdita_prima_B

ERRORI TIPICI
- w = w + lr * dw (segno sbagliato): la perdita sale.
- Aggiornare w e poi calcolare il gradiente di b con il NUOVO w: i due
  aggiornamenti devono usare lo STESSO gradiente, calcolato una volta sola
  PRIMA di aggiornare entrambi.
- Dimenticare di ricalcolare la perdita con i nuovi parametri.
- lr troppo grande (provalo con 0.1 sui dati reali): la perdita sale.

BONUS (facoltativo)
- Con un ciclo for esegui 10 passi di fila, stampando la perdita a ogni passo.
  Dovrebbe scendere ogni volta. E' quasi il training loop dell'esercizio 7.
- Prova lr = 0.001 e lr = 0.02 per un passo: confronta le perdite.
- Disegna la retta prima e dopo un passo sui dati.

Scrivi il tuo codice qui sotto.
"""

