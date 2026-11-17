"""Esercizio 9 (Modulo 3) - Verifica finale: il gradient descent trova la soluzione giusta?

Teoria: teoria/04_regressione_gradient_descent.md, sezioni 10 e 11.

OBIETTIVO
Controllare che i parametri trovati con il tuo gradient descent coincidano con
quelli della soluzione esatta dei minimi quadrati, e misurare la qualita' del
modello con R^2. Poi estendere a PIU' caratteristiche con le matrici.

PARTE A - CONFRONTO CON LA SOLUZIONE ESATTA
1. Addestra per 5000 epoche con lr = 0.01 (funzione addestra dell'esercizio 8).
       w = 2.0181    b = 0.6530
2. Calcola la soluzione esatta con NumPy:
       w_np, b_np = np.polyfit(x, y, 1)        -> 2.0181, 0.6530
3. Calcola la stessa soluzione con la formula chiusa:
       w_f = np.cov(x, y, bias=True)[0, 1] / np.var(x)
       b_f = np.mean(y) - w_f * np.mean(x)
4. Stampa i tre risultati affiancati: devono coincidere almeno a 4 cifre.
   Con soli 1000 epoche w e b sono 2.0189 e 0.6476: b ci mette di piu'. Perche'?
   (Perche' la valle e' piu' piatta nella direzione di b: vedi teoria, sezione 8.)

PARTE B - R^2 (QUALITA' DEL MODELLO)
       ss_res = np.sum((y - (w * x + b)) ** 2)
       ss_tot = np.sum((y - np.mean(y)) ** 2)
       r2 = 1 - ss_res / ss_tot          ->  circa 0.961
Interpretazione da scrivere in un commento: il modello spiega circa il 96% della
variabilita' di y. Cosa vale R^2 per un modello che prevede sempre la media?
(0). E per uno perfetto? (1.)
Calcola anche la correlazione np.corrcoef(x, y)[0, 1] (circa 0.980) e verifica
che R^2 e' il suo quadrato (0.980^2 = 0.961).

PARTE C - PIU' CARATTERISTICHE (matrici)
Genera dati con 3 feature:
    rng = np.random.default_rng(7)
    X = rng.normal(0, 1, (200, 3))
    w_vero = np.array([3.0, -2.0, 0.5])
    y = X @ w_vero + 4 + rng.normal(0, 0.5, 200)
Scrivi le versioni "matriciali":
    predici_m(X, w, b)  =  X @ w + b
    gradiente_m(X, y, w, b):
        e  = X @ w + b - y
        dw = 2 * (X.T @ e) / len(y)       # vettore con 3 elementi
        db = 2 * np.mean(e)
Addestra con w = np.zeros(3), b = 0, lr = 0.1, 500 epoche.
Risultato atteso: w = [3.03, -1.97, 0.49], b = 4.00 (vicini ai valori veri
[3, -2, 0.5] e 4; la differenza e' dovuta al rumore), perdita finale 0.251
(vicina alla varianza del rumore: 0.5^2 = 0.25).
Verifica con la formula esatta:  np.linalg.lstsq(np.c_[X, np.ones(200)], y, rcond=None)[0]

CONCETTI NUOVI
- Soluzione in forma chiusa (minimi quadrati) contro soluzione iterativa.
- R^2: frazione di variabilita' spiegata dal modello.
- Forma matriciale: ESATTAMENTE la stessa formula, per piu' feature.
- Quando la matematica esatta non e' disponibile (reti neurali) il gradient
  descent e' l'unico modo: e' quello che useremo nel Modulo 5.

COME VERIFICARE DA SOLO
    assert abs(w - w_np) < 1e-3 and abs(b - b_np) < 1e-3
    assert abs(w_f - w_np) < 1e-9
    assert abs(r2 - 0.961) < 0.002
    assert np.allclose(w_m, w_vero, atol=0.15) and abs(b_m - 4) < 0.15

ERRORI TIPICI
- Confrontare con troppe poche epoche e pensare che sia un errore.
- Non usare bias=True in np.cov: np.cov divide per N-1, np.var per N: le due
  scale non coincidono e w_f e' leggermente sbagliato.
- Confondere le forme: X.T @ e deve dare un vettore di 3 elementi.
- R^2 calcolato con segno sbagliato (ss_res / ss_tot senza "1 -").

BONUS (facoltativo)
- Standardizza le tre feature e confronta la velocita' di convergenza.
- Aggiungi una quarta feature irrilevante (solo rumore): quanto vale il suo
  peso imparato? (Dovrebbe essere vicino a zero.)
- Implementa il mini-batch: a ogni passo usa solo 32 campioni scelti a caso.
  La curva e' piu' rumorosa ma arriva allo stesso punto (teoria, sezione 9).
- Chiudi il modulo scrivendo in un file "modulo3/riassunto.md" 6-8 righe con
  parole tue: cos'e' un modello, la perdita, il gradiente, il learning rate.

Scrivi il tuo codice qui sotto.
"""

