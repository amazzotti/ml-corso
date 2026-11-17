"""Esercizio 1 (Modulo 3) - Dati su una retta.

Teoria: teoria/04_regressione_gradient_descent.md, sezioni 2 e 3.

OBIETTIVO
Generare un piccolo dataset "sintetico": punti che stanno quasi su una retta
y = 2x + 1, con un po' di rumore. Su questi dati faremo, in tutti gli esercizi
del modulo, il nostro primo addestramento.

IL CODICE PER GENERARE I DATI (identico in tutti gli esercizi del modulo!)
    import numpy as np
    rng = np.random.default_rng(42)
    x = rng.uniform(0, 10, 50)
    y = 2 * x + 1 + rng.normal(0, 1.5, 50)
Scrivilo tu: con lo stesso seed 42 otterrai SEMPRE gli stessi 50 punti, quindi
anche i numeri attesi sotto saranno sempre gli stessi.

PASSI
1. Genera x e y come sopra.
2. Stampa le loro forme (.shape) e le prime 3 coppie (x, y).
3. Stampa media e deviazione standard di x e di y.
4. Disegna lo scatter dei punti con matplotlib e sovrapponi la RETTA VERA
   y = 2x + 1 (una linea sui punti). Titolo, etichette degli assi, legenda.
5. Salva il grafico in modulo3/grafici/01_dati.png
   (come nell'esercizio 7 del Modulo 2; la cartella "grafici" e' ignorata da git).

RISULTATI ATTESI
    x.shape = y.shape = (50,)
    prime 3 coppie:  x = 7.740, 4.389, 8.586   y = 17.497, 9.879, 18.606
    media di x = 5.352     media di y = 11.455
Il grafico mostra una nuvola di punti lungo una retta crescente; i punti non
stanno esattamente sulla retta.

VOCABOLARIO IN PRATICA (scrivilo in un commento, con parole tue)
- Quanti sono i CAMPIONI? (50)
- Qual e' la CARATTERISTICA (feature)? (x)
- Qual e' l'ETICHETTA (label)? (y)
- Cos'e' il rumore, e perche' lo aggiungiamo?
  (Nei dati reali nulla sta esattamente su una retta.)

CONCETTI NUOVI
- Dataset sintetico con retta vera + rumore gaussiano.
- Campione, feature, etichetta (teoria sezione 2).
- Il modello NON conosce i valori veri (2 e 1): dovra' ricavarli dai dati.

COME VERIFICARE DA SOLO
    assert x.shape == (50,) and y.shape == (50,)
    assert abs(x.mean() - 5.352) < 0.001
    assert abs(y.mean() - 11.455) < 0.001
    assert abs(x[0] - 7.740) < 0.001 and abs(y[0] - 17.497) < 0.001

ERRORI TIPICI
- Dimenticare il seed o cambiarlo: i numeri cambiano e gli assert sbagliano.
- Usare rng.normal(0, 1.5) senza il terzo argomento (50): ottieni UN solo
  numero di rumore, uguale per tutti i punti (y e' una retta perfetta, piu' un
  salto costante).
- Disegnare la retta con pochi punti: usa np.linspace(0, 10, 100).

BONUS (facoltativo)
- Cambia il livello di rumore (0.1, 1.5, 5) e osserva come cambia il grafico.
  Che cosa succede se il rumore e' molto grande?
- Genera 500 punti invece di 50.
- Genera dati che seguono y = -3x + 7 e confronta.

Scrivi il tuo codice qui sotto.
"""

