"""Esercizio 3 (Modulo 5) - Il perceptron: AND, OR e il muro di XOR.

Teoria: teoria/06_reti_neurali.md, sezione 7.

OBIETTIVO
Addestrare un singolo neurone con la regola del perceptron a imparare AND e OR, e
scoprire sperimentalmente che NON riesce a imparare XOR.

DATI
       X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
       y_and = [0, 0, 0, 1]
       y_or  = [0, 1, 1, 1]
       y_xor = [0, 1, 1, 0]

IL NEURONE E LA REGOLA
Previsione:   p = 1 se  w . x + b > 0,  altrimenti 0     (attivazione a gradino)
Per ogni campione:
       e = target - p
       w = w + lr * e * x
       b = b + lr * e
Se la previsione e' giusta (e = 0) non cambia nulla; se e' sbagliata il neurone si
sposta per correggere.

PASSI
1. Scrivi  addestra_perceptron(X, y, lr=0.1, max_epoche=100):
   - parte da w = [0, 0], b = 0;
   - a ogni epoca scorre i 4 campioni NELL'ORDINE dato e applica la regola;
   - conta gli errori dell'epoca; se sono 0 si ferma e restituisce (w, b, epoca);
   - se non converge entro max_epoche restituisce (w, b, None).
2. Risultati attesi (lr = 0.1, ordine dei campioni come sopra):
       AND:  converge all'epoca 6   w = [0.2, 0.1]   b = -0.2
       OR:   converge all'epoca 4   w = [0.1, 0.1]   b = 0.0
       XOR:  NON converge entro 100 epoche (restituisce None)
   Verifica le tabelle di verita': per AND con w = [0.2, 0.1] e b = -0.2:
       (0,0): -0.2 -> 0     (0,1): -0.1 -> 0     (1,0): 0.0 -> 0     (1,1): 0.1 -> 1
   (Attenzione al caso z = 0: con "z > 0" vale 0.)
3. Per ciascun problema stampa la previsione del neurone per i 4 campioni.
4. Disegna i 4 punti per XOR (colore = classe) e prova a tracciare A MANO una retta che
   separi i punti verdi da quelli rossi. Non ci riesci: i punti stanno agli angoli opposti
   di un quadrato. Scrivi in un commento perche' un singolo neurone (che divide il
   piano con una retta) non puo' farcela.
5. Disegna lo stesso grafico per AND e OR e traccia la retta imparata: w1*x1 + w2*x2 + b = 0
   cioe' x2 = -(w1*x1 + b) / w2.

CONCETTI NUOVI
- Perceptron: neurone + gradino + regola di aggiornamento.
- Separabilita' lineare: AND e OR si, XOR no.
- Convergenza garantita (per dati linearmente separabili), mai per XOR.
- Per XOR serve uno strato NASCOSTO (prossimo esercizio).

COME VERIFICARE DA SOLO
    w, b, ep = addestra_perceptron(X, np.array([0, 0, 0, 1]))
    assert ep == 6 and np.allclose(w, [0.2, 0.1]) and abs(b + 0.2) < 1e-9
    w, b, ep = addestra_perceptron(X, np.array([0, 1, 1, 1]))
    assert ep == 4 and np.allclose(w, [0.1, 0.1]) and abs(b) < 1e-9
    w, b, ep = addestra_perceptron(X, np.array([0, 1, 1, 0]))
    assert ep is None

ERRORI TIPICI
- Dimenticare di aggiornare anche il bias.
- Usare ">=" invece di ">" nel gradino: cambia i risultati nei casi limite (z = 0)
  e potresti non ritrovare esattamente i numeri attesi.
- Mescolare l'ordine dei campioni: i valori esatti dipendono dall'ordine.
- Interrompere troppo presto (max_epoche piccolo) e concludere che non converge.
- Aggiornare con (previsione - target) invece di (target - previsione): il neurone
  si allontana dalla soluzione.

BONUS (facoltativo)
- Prova AND con ingressi in {-1, +1}: cambia qualcosa?
- Provando le porte NAND e NOR: sono tutte linearmente separabili?
- Risolvi XOR "a mano" combinando perceptron: XOR = (x1 OR x2) AND NOT (x1 AND x2).
  Costruiscilo con tre perceptron (due nascosti e uno di uscita), con pesi scelti da te:
  e' esattamente l'idea di una rete a due strati.

Scrivi il tuo codice qui sotto.
"""

