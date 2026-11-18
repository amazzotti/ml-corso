"""Esercizio 4 (Modulo 5) - Una rete a due strati che impara XOR, con backpropagation scritta a mano.

Teoria: teoria/06_reti_neurali.md, sezioni 3, 4, 5 e 6.

OBIETTIVO
Costruire con soli NumPy una rete con uno strato nascosto, calcolare a mano la
backpropagation e addestrarla a risolvere XOR, il problema che un singolo neurone
non riesce a imparare. E' l'esercizio piu' importante del modulo.

ARCHITETTURA
       ingresso (2)  ->  nascosto (4 neuroni, sigmoide)  ->  uscita (1 neurone, sigmoide)
       X: (4, 2)     W1: (2, 4), b1: (4,)               W2: (4, 1), b2: (1,)
Parametri totali: 2*4 + 4 + 4*1 + 1 = 17.

DATI
       X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
       Y = np.array([[0], [1], [1], [0]], dtype=float)

INIZIALIZZAZIONE (riproducibile)
       rng = np.random.default_rng(0)
       W1 = rng.normal(0, 1, (2, 4));  b1 = np.zeros(4)
       W2 = rng.normal(0, 1, (4, 1));  b2 = np.zeros(1)
Perche' non tutti zeri? Tutti i neuroni nascosti farebbero la stessa cosa (simmetria).

IL CICLO (per ogni epoca)
FORWARD
       H = sigmoide(X @ W1 + b1)                  # (4, 4)
       out = sigmoide(H @ W2 + b2)                # (4, 1)
       perdita = np.mean((out - Y) ** 2)
BACKWARD (dall'uscita all'ingresso: regola della catena)
       d_out = 2 * (out - Y) / len(Y) * out * (1 - out)      # (4, 1)
       dW2 = H.T @ d_out                                      # (4, 1)
       db2 = d_out.sum(axis=0)                                # (1,)
       d_H = (d_out @ W2.T) * H * (1 - H)                     # (4, 4)
       dW1 = X.T @ d_H                                        # (2, 4)
       db1 = d_H.sum(axis=0)                                  # (4,)
AGGIORNAMENTO
       W1 -= lr * dW1;  b1 -= lr * db1;  W2 -= lr * dW2;  b2 -= lr * db2
con lr = 1.0 e 10000 epoche.

Spiegazione a parole del backward (da riscrivere come commento nel codice):
- d_out: quanto la perdita cambia al variare di z dell'uscita (catena: perdita ->
  uscita -> sigmoide).
- dW2: l'errore dell'uscita combinato con cio' che i neuroni nascosti hanno prodotto.
- d_H: l'errore "torna indietro" attraverso i pesi W2 e viene moltiplicato per la
  derivata della sigmoide dello strato nascosto.
- dW1: l'errore del nascosto combinato con gli ingressi.

PASSI
1. Scrivi il ciclo e registra la perdita a ogni epoca in una lista.
2. Perdita attesa (seed 0):
       epoca     1:  0.343
       epoca   100:  0.2497      (quasi ferma: la rete e' ancora "indecisa")
       epoca  1000:  0.0238
       epoca  5000:  0.0008
       epoca 10000:  0.0003
   Nelle prime epoche la perdita resta intorno a 0.25 (la rete risponde ~0.5 a tutto),
   poi crolla: la rete ha "trovato" la struttura di XOR. E' tipico e istruttivo.
3. Uscite finali per i 4 ingressi (seed 0):
       [0.007, 0.981, 0.981, 0.024]   cioe' ~[0, 1, 1, 0]   -> XOR risolto!
4. Disegna la curva della perdita (asse y in scala logaritmica).
5. GRADIENT CHECK: prima di addestrare, verifica che dW1[0, 0] coincida con la derivata
   numerica rispetto a W1[0, 0]:
       eps = 1e-6
       W1[0, 0] += eps; L_piu = perdita(...); W1[0, 0] -= 2 * eps; L_meno = perdita(...)
       W1[0, 0] += eps    # ripristina
       numerica = (L_piu - L_meno) / (2 * eps)
   I due valori devono coincidere almeno a 6 cifre. E' il modo per scoprire errori nelle
   formule della backpropagation.
6. Disegna il "paesaggio" di decisione: calcola l'uscita della rete su una griglia di punti
   (x1, x2) in [0,1] x [0,1] e usa plt.contourf. Vedrai due regioni "a fascia": la rete ha
   imparato un confine NON lineare, impossibile per un singolo neurone.
7. Prova a RIPETERE con altri seed (da 1 a 7): tutti imparano XOR con questi iperparametri.
   Prova anche con meno neuroni nascosti (cambia le forme: W1 (2, h), W2 (h, 1)):
       h = 1: non impara mai (0 seed su 8)
       h = 2: impara in 5 seed su 8 (dipende dall'inizializzazione!)
       h = 4: impara in tutti gli 8 seed
   Con 1 neurone nascosto la rete e' di fatto un modello quasi lineare e non puo'
   separare XOR; con 2 il problema e' risolvibile ma l'addestramento puo' bloccarsi;
   con 4 e' robusto. Scrivi cosa deduci sull'importanza della dimensione dello strato.
8. In un commento rispondi: cosa fanno i neuroni nascosti? (Costruiscono una nuova
   rappresentazione degli ingressi in cui le due classi diventano separabili.)

CONCETTI NUOVI
- Propagazione in avanti e perdita di una rete a due strati.
- Backpropagation con la regola della catena, strato per strato.
- Gradient check (derivata numerica contro derivata analitica).
- Inizializzazione casuale dei pesi; il ruolo dello strato nascosto.
- Iperparametri: numero di neuroni nascosti, learning rate, epoche.

COME VERIFICARE DA SOLO
    assert abs(storia[0] - 0.343) < 0.01
    assert storia[-1] < 0.001
    assert ((out > 0.5).astype(int).ravel() == [0, 1, 1, 0]).all()
    assert abs(dW1_analitico - dW1_numerico) < 1e-6
    # parametri totali
    assert W1.size + b1.size + W2.size + b2.size == 17

ERRORI TIPICI
- Dimenticare la derivata della sigmoide (out * (1 - out) e H * (1 - H)).
- Dimenticare il fattore 2/N nel gradiente della perdita (MSE).
- Forme sbagliate: usa .shape di ogni array se compare un errore di prodotto matriciale
  (H.T @ d_out deve essere (4, 1), X.T @ d_H deve essere (2, 4)).
- Segno di aggiornamento: devono essere "-=".
- Calcolare d_H con W2 gia' aggiornato: usa i pesi PRIMA dell'aggiornamento (calcola tutti
  i gradienti, poi aggiorna).
- Non vedere la perdita scendere nelle prime 100 epoche e pensare a un bug: e' normale
  (plateau iniziale).

BONUS (facoltativo)
- Sostituisci la sigmoide dello strato nascosto con la tanh o con la ReLU (e la derivata
  corrispondente, teoria sezione 2). Come cambiano le epoche necessarie?
- Cambia la perdita in cross-entropy binaria: la derivata d_out si semplifica a
  (out - Y) / N (provalo e verifica che la rete impari piu' in fretta).
- Aggiungi un secondo strato nascosto: ecco una rete "profonda". Il backward ha un passaggio
  in piu', identico agli altri.
- Allena la rete per imparare la funzione XNOR o la parita' di 3 bit (8 campioni).

Scrivi il tuo codice qui sotto.
"""

