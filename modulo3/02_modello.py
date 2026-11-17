"""Esercizio 2 (Modulo 3) - Il modello: una retta con due parametri.

Teoria: teoria/04_regressione_gradient_descent.md, sezione 3.

OBIETTIVO
Scrivere il modello  y_pred = w * x + b  come funzione e vedere cosa succede
cambiando i parametri w (pendenza) e b (intercetta) rispetto ai dati.

DATI
Genera x e y come nell'esercizio 1 (seed 42, 50 punti, y = 2x + 1 + rumore).

PASSI
1. Scrivi la funzione:
       def predici(x, w, b):
           return w * x + b
   Funziona con un numero singolo o con un intero array NumPy.
2. Prova:  predici(np.array([0, 1, 2]), 2, 1)  deve dare  [1 3 5].
3. Disegna in UNA figura lo scatter dei dati e quattro rette, ciascuna con
   la sua legenda, usando x_linea = np.linspace(0, 10, 100):
       (w, b) = (0, 0)     una retta piatta sullo zero
       (1, 0)              troppo poco pendente
       (3, -5)             troppo pendente e troppo bassa
       (2, 1)              i parametri veri
4. Guarda il grafico: quale retta sembra la migliore? Scrivilo in un commento.
5. Per ogni coppia calcola a mano, con un print, la previsione per x = 5:
       (0, 0) -> 0      (1, 0) -> 5      (3, -5) -> 10      (2, 1) -> 11

CONCETTI NUOVI
- Un MODELLO e' una funzione con PARAMETRI. Qui: w e b.
- Imparare vuol dire trovare i valori dei parametri giusti.
- w (peso): di quanto aumenta y_pred quando x aumenta di 1.
- b (bias): il valore di y_pred quando x = 0.
- Vettorializzazione: la stessa funzione lavora su tutti i campioni, senza cicli.

COME VERIFICARE DA SOLO
    assert list(predici(np.array([0, 1, 2]), 2, 1)) == [1, 3, 5]
    assert predici(5, 0, 0) == 0 and predici(5, 1, 0) == 5
    assert predici(5, 3, -5) == 10 and predici(5, 2, 1) == 11
    assert predici(x, 2, 1).shape == x.shape

ERRORI TIPICI
- Scrivere w * x + b con x una lista Python: [1, 2] * 3 ripete la lista! Serve
  un array NumPy.
- Confondere i parametri (w, b: che si imparano) con i dati (x, y: che sono
  dati e non cambiano).
- Dimenticare di chiamare plt.legend().

BONUS (facoltativo)
- Aggiungi un controllo visivo "a occhio": prova a trovare a tentativi una
  coppia (w, b) che sembri andare bene. Quanti tentativi ti servono?
  (Nel prossimo esercizio misureremo "quanto bene" con un numero e poi
  lasceremo trovare i valori al computer.)
- Disegna 20 rette con valori di w e b casuali sullo stesso grafico.

Scrivi il tuo codice qui sotto.
"""

