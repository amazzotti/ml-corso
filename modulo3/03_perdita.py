"""Esercizio 3 (Modulo 3) - La funzione di perdita (errore quadratico medio).

Teoria: teoria/04_regressione_gradient_descent.md, sezione 4.

OBIETTIVO
Misurare con UN numero quanto una retta sbaglia sui dati, e vedere come questo
numero cambia al variare dei parametri.

DATI E MODELLO
Dati: come nell'esercizio 1 (seed 42). Modello: predici(x, w, b) dell'esercizio 2.

PASSI
1. Scrivi la funzione:
       def mse(y_pred, y_vero):
           return np.mean((y_pred - y_vero) ** 2)
   Per ogni campione: errore = previsione - valore vero; poi al quadrato;
   poi la media di tutti.
2. Prova a MANO con un esempio piccolo:
       mse(np.array([0, 0, 0]), np.array([2, 4, 6]))   ->  18.666...
   Verifica il calcolo: (4 + 16 + 36) / 3.
3. Calcola la perdita sui 50 dati per queste coppie (w, b):
       (0, 0)  ->  163.94
       (1, 0)  ->   46.53
       (2, 1)  ->    1.355   (i parametri veri: non zero a causa del rumore!)
   Osserva: la perdita e' piu' bassa quando la retta e' piu' vicina ai dati.
4. Fissa b = 1 e calcola la perdita per 200 valori di w tra -1 e 5:
       ws = np.linspace(-1, 5, 200)
       perdite = [mse(predici(x, w, 1), y) for w in ws]
   Disegna perdite contro ws: una curva a U (una parabola). Aggiungi una linea
   verticale tratteggiata a w = 2.
5. Trova il w con la perdita minima:
       ws[np.argmin(perdite)]      -> circa 1.95 (vicino a 2)
   Spiega in un commento perche' non e' ESATTAMENTE 2 (rumore nei dati,
   e b fissato a 1 che non e' l'ottimo).

CONCETTI NUOVI
- Errore = previsione - valore vero.
- Perche' il QUADRATO: nessuna cancellazione tra errori positivi e negativi,
  penalizza molto gli errori grandi, funzione liscia e derivabile.
- MSE (mean squared error) = media dei quadrati degli errori.
- La perdita e' una funzione dei PARAMETRI: L(w, b). I dati sono fissi.
- Il "paesaggio": ogni coppia (w, b) e' un punto, la perdita e' la quota.
  Addestrare = scendere verso il fondo della valle.

COME VERIFICARE DA SOLO
    assert abs(mse(np.array([0, 0, 0]), np.array([2, 4, 6])) - 18.6667) < 1e-3
    assert abs(mse(predici(x, 0, 0), y) - 163.94) < 0.01
    assert abs(mse(predici(x, 1, 0), y) - 46.53) < 0.01
    assert abs(mse(predici(x, 2, 1), y) - 1.355) < 0.001
    assert abs(ws[np.argmin(perdite)] - 2) < 0.3

ERRORI TIPICI
- Usare np.sum invece di np.mean: la perdita dipende dal numero di campioni.
- Dimenticare il quadrato (la somma degli errori si cancella).
- Calcolare la perdita con y_pred e y scambiati: funziona lo stesso (il quadrato
  non cambia), ma tieni un ordine fisso per non confondere i segni quando
  calcolerai il gradiente.
- Passare a mse una lista invece di un array.

BONUS (facoltativo)
- Scrivi anche mae(y_pred, y_vero) = np.mean(np.abs(y_pred - y_vero)) e
  confronta le due perdite sulle stesse coppie. Quale cresce piu' in fretta
  quando l'errore e' grande?
- Disegna la perdita su una griglia di (w, b) con un grafico a curve di
  livello:  plt.contourf(W, B, L)  con  W, B = np.meshgrid(ws, bs).
  Vedrai una valle ovale: il minimo e' al centro.
- Aggiungi un punto anomalo (x = 5, y = 100) e osserva come cambia la
  perdita MSE contro MAE: l'outlier pesa molto di piu' nel MSE.

Scrivi il tuo codice qui sotto.
"""

