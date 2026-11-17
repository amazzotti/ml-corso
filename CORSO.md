# Quaderno del corso di Machine Learning

Documento di continuità: raccoglie obiettivo, metodo, piano completo e stato di avanzamento.
Chi lo legge (io stesso, un tutor, un collega) deve poter capire
**cosa è stato fatto, cosa no e qual è il prossimo passo** senza altre informazioni.
Si aggiorna alla fine di ogni sessione (sezione 6).

---

## 1. Obiettivo e punto di partenza

- Imparo il machine learning **partendo da zero**: programmazione (Python), teoria e pratica
  dell'addestramento di reti neurali.
- Arrivare a un **primo progetto completo** (classificatore di cifre scritte a mano, MNIST,
  oppure un progetto su dati scelti da me).
- Livello di partenza: nessuna esperienza in ML. Non dare nulla per scontato:
  spiegare ogni termine alla prima occorrenza.
- Lingua: **italiano**. Spiegazioni brevi, concrete, con esempio di codice.

## 2. Metodo di lavoro (da rispettare)

1. Si introduce **un concetto alla volta**, in poche righe, con un esempio.
2. Segue **un esercizio piccolo**. Il codice lo scrivo **io**, non chi mi guida.
3. Si esegue, si leggono insieme gli errori. Se sono bloccato: prima un **suggerimento**,
   poi, solo se serve, la soluzione commentata.
4. La teoria (derivate, probabilità, gradiente, funzione di perdita) entra **quando serve**,
   sempre accanto a codice che la usa. Non serve matematica avanzata.
5. Ogni esercizio è un file **già creato** da chi guida, con la descrizione in testa (obiettivo,
   concetti nuovi, suggerimento) in modo che io lo legga direttamente da VS Code; il codice lo
   scrivo io sotto la descrizione. Il file è numerato nella cartella del modulo, per esempio
   `modulo1/03_liste.py`. Ogni file inizia con un commento che dice cosa dimostra.
6. A fine sessione: commit, push, e aggiornamento della sezione 8.

## 3. Piano completo dei moduli

### Modulo 0 — Setup e primo programma
- Python 3.12, VS Code con estensione Python, ambiente virtuale `.venv`, Git.
- Concetti: cos'è un interprete, come si esegue un file, cos'è un ambiente virtuale.
- Esercizi: `01_ciao.py` (stampare una frase); `02_input.py` (chiedere il nome e salutare).

### Modulo 1 — Python base
- Argomenti: variabili e tipi, operatori, `if/else`, liste, tuple, dizionari, cicli `for` e
  `while`, funzioni, lettura/scrittura file, errori e `try/except`.
- Esercizi: indovina-il-numero, contatore di parole in un testo, convertitore di unità,
  FizzBuzz, rubrica con dizionario. Fine modulo: piccolo programma che combina tutto.

### Modulo 2 — Strumenti per i dati
- NumPy (array, operazioni vettoriali, matrici), pandas (tabelle, filtri, medie, raggruppamenti),
  matplotlib (grafici a linee, istogrammi, dispersione).
- Esercizi: statistiche su un array, caricare un CSV, ripulire dati mancanti, 3 grafici.

### Modulo 3 — Primo modello a mano: regressione lineare
- Idea di modello (una funzione con parametri), funzione di perdita (errore quadratico medio),
  derivata e gradiente, **gradient descent**, learning rate.
- Tutto scritto **solo con NumPy**, senza librerie di ML.
- Esercizi: generare punti rumorosi su una retta; calcolare la perdita; fare un passo di
  gradient descent a mano; ciclo completo; grafico della perdita che scende.
- È il modulo più importante: rende comprensibile tutto ciò che segue.

### Modulo 4 — Machine learning classico (scikit-learn)
- Train/test split, overfitting e underfitting, classificazione, regressione logistica,
  alberi decisionali, metriche (accuratezza, precisione, recall, matrice di confusione).
- Esercizi: dataset Iris, poi un dataset più sporco; confrontare due modelli.

### Modulo 5 — Reti neurali
- Neurone, funzioni di attivazione, strati, propagazione in avanti, **backpropagation**.
- Prima un perceptron scritto a mano (rete che impara XOR), poi PyTorch: tensori,
  autograd, `nn.Module`, ottimizzatori, ciclo di training, GPU/CPU.
- Esercizi: neurone a mano; XOR; stessa rete in PyTorch; confronto dei risultati.

### Modulo 6 — Primo progetto
- Classificatore di cifre scritte a mano (MNIST) con una rete in PyTorch, valutazione su
  dati di test, analisi degli errori, breve relazione dei risultati.
- In alternativa: progetto su dati scelti da me, concordato prima.

## 4. Struttura del repository

```
ml-corso/
  CORSO.md            questo quaderno
  README.md           descrizione breve
  requirements.txt    dipendenze, aggiornato quando servono
  .gitignore          esclude .venv/, __pycache__/, data/, modelli pesanti
  modulo0/ ... modulo6/
```

## 5. Regole per commit e file

- Messaggi di commit brevi, in italiano, in prima persona dell'autore, ad esempio
  "Aggiungo esercizi su liste e cicli".
- Prima di ogni push: `git status`, controllare che `.venv/` e i dati pesanti non siano inclusi.
- Prima di iniziare a lavorare: `git pull`. A fine sessione: `git add`, `git commit`, `git push`.

## 6. Stato di avanzamento

Legenda: [x] fatto, [ ] da fare.

- [x] Modulo 0 — completato: `01_ciao.py` (print), `02_input.py` (input e variabili), `03_eta.py` (int e f-string), `04_calcolatrice.py` (float, operatori, ZeroDivisionError visto)
- [ ] Modulo 1 — in corso. File creato: `modulo1/01_condizioni.py` (if/elif/else), da svolgere
- [ ] Modulo 2
- [ ] Modulo 3
- [ ] Modulo 4
- [ ] Modulo 5
- [ ] Modulo 6

**Ultima sessione: 2026-11-17.** Completato il Modulo 0. **Prossimo passo:** Modulo 1, primo esercizio
`modulo1/01_condizioni.py`: `if/elif/else` e confronti (es. dire se un numero e' positivo, negativo o zero).
