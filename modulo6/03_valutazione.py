"""Progetto (Modulo 6) - Passo 3: valutare la rete sul test set.

Teoria: teoria/05_ml_classico.md, sezione 7; teoria/06_reti_neurali.md, sezione 9.

OBIETTIVO
Valutare seriamente il modello: accuratezza globale, matrice di confusione 10 x 10,
precisione e recall per ogni cifra, e capire quali cifre la rete confonde.

PREPARAZIONE
Ricostruisci la stessa architettura del passo 2 e carica i pesi salvati:
       rete = Rete()                       # la classe del passo 2 (puoi copiarla qui)
       rete.load_state_dict(torch.load(Path(__file__).parent / "modello.pt"))
       rete.eval()
Se non vuoi ripetere l'addestramento, il file modello.pt arriva dal passo 2. Se non esiste,
ripeti prima il passo 2.

PASSI
1. Raccogli le previsioni su tutto il test set:
       tutte_prev, tutte_vere = [], []
       with torch.no_grad():
           for X, y in dati_test:
               tutte_prev.append(rete(X).argmax(dim=1))
               tutte_vere.append(y)
       prev = torch.cat(tutte_prev).numpy();  vere = torch.cat(tutte_vere).numpy()
2. Accuratezza globale: (prev == vere).mean() -> tra 0.971 e 0.978 (quella dell'ultima epoca
   del passo 2; in una esecuzione di riferimento 0.973).
   Numero di errori: tra 220 e 290 su 10.000 (2,2-2,9%); nella esecuzione di riferimento 272.
3. Matrice di confusione 10 x 10:
       from sklearn.metrics import confusion_matrix, classification_report
       cm = confusion_matrix(vere, prev)
   Verifica: cm.sum() == 10000 e cm.trace() == numero di previsioni corrette.
   Righe = cifra vera, colonne = cifra prevista; la diagonale e' tutto cio' che e' giusto.
4. Disegnala come mappa di colore (ax.imshow(cm) con colorbar, etichette 0-9 sugli assi,
   il numero in ogni cella). Salva in modulo6/grafici/03_confusione.png.
   Per vedere meglio gli errori, azzera la diagonale e ridisegna: restano solo le confusioni.
5. Trova le 5 coppie (vera -> prevista) piu' frequenti negli errori:
       cm_err = cm.copy();  np.fill_diagonal(cm_err, 0)
       ordina gli indici di cm_err.ravel() in ordine decrescente
   Nella esecuzione di riferimento le piu' frequenti sono (vera -> prevista, conteggio):
       4 -> 9 (33), 7 -> 9 (18), 8 -> 3 (13), 5 -> 3 (12), 3 -> 9 (9), 7 -> 2 (8)
   cioe' cifre dalla forma simile. (L'elenco esatto dipende dall'addestramento, ma 4 -> 9
   e' in genere la piu' frequente.)
6. Precisione, recall e F1 per cifra:
       print(classification_report(vere, prev, digits=3))
   Nella esecuzione di riferimento il recall va da 0.949 (cifre 4 e 8) a 0.989 (cifra 1);
   gli altri valori stanno intorno a 0.97-0.98. Quale cifra ha il recall piu' basso?
   Quale la precisione piu' bassa? Scrivi in un commento una spiegazione plausibile
   guardando le coppie del punto 5.
7. Confronta con il riferimento banale (risposta sempre "1": 11,35% sul test set) e con la
   regressione logistica di scikit-learn su pixel appiattiti, se hai voglia (bonus):
   un classificatore lineare su MNIST arriva a circa il 92%; la rete a oltre il 97%.
8. Scrivi in un commento una frase di sintesi con il numero giusto di cifre decimali:
   "La rete riconosce circa il 97,3% delle cifre del test set (272 errori su 10.000)". Non scrivere
   12 decimali: la stima ha un'incertezza (con 10.000 campioni e p = 0,973 circa +-0,3%) e
   cambia di un paio di decimi di punto cambiando seed.

CONCETTI NUOVI
- Matrice di confusione multiclasse e come leggerla.
- Metriche per classe (precisione, recall, F1) con classification_report.
- Analisi delle confusioni: quali classi si scambiano e perche'.
- Incertezza di una stima di accuratezza.

COME VERIFICARE DA SOLO
    assert cm.shape == (10, 10) and cm.sum() == 10000
    assert cm.trace() == (prev == vere).sum()
    assert 0.968 < (prev == vere).mean() < 0.985
    assert (prev != vere).sum() == 10000 - cm.trace()

ERRORI TIPICI
- Valutare sul training set invece che sul test set.
- Dimenticare rete.eval() (con dropout le previsioni sarebbero casuali).
- Dimenticare .numpy() prima di passare ai grafici di matplotlib / scikit-learn.
- Leggere righe e colonne della matrice scambiate.
- Caricare i pesi su un'architettura diversa (errore "size mismatch").
- Riportare l'accuratezza con troppe cifre decimali.

BONUS (facoltativo)
- Calcola l'accuratezza per cifra (diagonale / somma della riga) e disegna un grafico a barre.
- Addestra una LogisticRegression di scikit-learn su immagini appiattite e confrontala.
- Calcola un intervallo di confidenza approssimato: p +- 1.96 * sqrt(p(1-p)/N).

Scrivi il tuo codice qui sotto.
"""

