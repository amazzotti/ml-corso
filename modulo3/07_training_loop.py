"""Esercizio 7 (Modulo 3) - Il ciclo di addestramento completo.

Teoria: teoria/04_regressione_gradient_descent.md, sezioni 7, 9 e 11.

OBIETTIVO
Ripetere il passo di gradient descent per molte epoche, registrare la perdita
a ogni epoca e disegnare la curva: il tuo primo VERO addestramento di un modello.

DATI
50 punti con seed 42 (esercizio 1). Funzioni: predici, mse, gradiente.

STRUTTURA
    w, b = 0.0, 0.0
    lr = 0.01
    epoche = 1000
    storia = []                      # la perdita a ogni epoca
    for epoca in range(epoche):
        dw, db = gradiente(x, y, w, b)
        w = w - lr * dw
        b = b - lr * db
        storia.append(mse(predici(x, w, b), y))

PASSI
1. Scrivi il ciclo come sopra.
2. Stampa la perdita alle epoche 1, 10, 100, 500, 1000.
   Valori attesi (con lr = 0.01):
       epoca    1 :  12.04
       epoca   10 :   1.314
       epoca  100 :   1.301
       epoca  500 :   1.291
       epoca 1000 :   1.290
   La perdita crolla nelle prime epoche e poi si stabilizza.
3. Stampa i parametri finali:
       w = 2.019    b = 0.648
   (I valori VERI usati per generare i dati erano 2 e 1: il modello li ha
   "imparati" dai dati. Il rumore impedisce di ritrovarli esattamente;
   b e' meno preciso perche' ha meno "leva" sui dati.)
4. Disegna in una figura con due grafici affiancati (subplots 1 x 2):
   a sinistra la CURVA DELLA PERDITA (storia contro epoca), a destra i dati
   con la retta finale (e, tratteggiata, la retta vera 2x + 1).
   Prova anche la scala logaritmica sull'asse y della perdita: ax.set_yscale("log").
5. Salva in modulo3/grafici/07_training.png.

CONCETTI NUOVI
- Epoca: un passaggio sui dati (qui: tutti i 50 campioni a ogni passo).
- Addestramento (training) = ripetere  gradiente -> aggiornamento -> perdita.
- Curva della perdita: lo strumento principale per capire se l'addestramento va bene.
- Convergenza: la perdita smette di scendere.
- La storia della perdita si registra per DIAGNOSTICA (non influenza l'addestramento).

COME VERIFICARE DA SOLO
    assert abs(w - 2.019) < 0.01 and abs(b - 0.648) < 0.05
    assert abs(storia[-1] - 1.290) < 0.01
    assert abs(storia[0] - 12.04) < 0.05
    # la perdita non deve mai salire (con lr = 0.01)
    assert all(storia[i + 1] <= storia[i] + 1e-12 for i in range(len(storia) - 1))

ERRORI TIPICI
- La perdita sale o diventa nan: learning rate troppo grande o segno sbagliato.
- La perdita non scende: aggiornamento dimenticato (w e b mai riassegnati).
- Calcolare la perdita PRIMA dell'aggiornamento e fare confusione sul numero di
  epoche: scegli un ordine e restaci coerente.
- Ricreare w e b a zero dentro il ciclo (devono nascere FUORI dal ciclo).
- Confondere "storia" (lista della perdita) con "w" (parametro).

BONUS (facoltativo)
- Aggiungi un criterio di arresto: ferma l'addestramento quando la perdita
  scende meno di 1e-8 rispetto all'epoca precedente (break). Dopo quante
  epoche succede? (Circa alla 1200esima con lr = 0.01.)
- Allena per 5000 epoche: w e b arrivano a 2.0181 e 0.6530, gli stessi di np.polyfit
  (esercizio 9).
- Parti da w = -10, b = 10 invece che da zero: la curva e' diversa, ma finisce
  nello stesso punto (il paesaggio ha un solo fondo).
- Disegna la retta ogni 100 epoche con colori sempre piu' scuri: vedrai la
  retta "assestarsi" sui dati.

Scrivi il tuo codice qui sotto.
"""

