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
6. A fine sessione: commit, push, e aggiornamento delle sezioni 6 e 7.

## 3. Piano completo dei moduli

### Modulo 0 — Setup e primo programma
- Python 3.12, VS Code con estensione Python, ambiente virtuale `.venv`, Git.
- Concetti: cos'è un interprete, come si esegue un file, cos'è un ambiente virtuale.
- Esercizi: vedi sezione 7.

### Modulo 1 — Python base
- Argomenti: variabili e tipi, operatori, `if/else`, liste, tuple, dizionari, cicli `for` e
  `while`, funzioni, lettura/scrittura file, errori e `try/except`.
- Esercizi: 12 file, vedi sezione 7 (indovina-il-numero, contatore di parole, convertitore di unità,
  FizzBuzz, rubrica con dizionario). Fine modulo: piccolo programma che combina tutto.

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

## 5b. Teoria

Gli appunti di teoria sono in file separati nella cartella `teoria/`, uno per argomento,
così si rileggono senza passare dal piano. Ogni file di teoria si scrive **quando si arriva**
all'argomento, in modo che corrisponda a ciò che è stato visto negli esercizi.

- [x] `teoria/01_python_base.md` — variabili, tipi, `input`, f-string, operatori, condizioni,
  cicli, liste, dizionari, lettura degli errori (Moduli 0 e 1).
- [x] `teoria/02_python_avanzato.md` — funzioni, file, `try/except`, moduli (fine Modulo 1).
- [x] `teoria/03_numpy_pandas.md` — array, vettori, matrici, tabelle, grafici (Modulo 2).
- [x] `teoria/04_regressione_gradient_descent.md` — campione, feature, etichetta, modello,
  perdita, gradiente, learning rate, addestramento (Modulo 3).
- [x] `teoria/05_ml_classico.md` — train/test, overfitting, classificazione, metriche (Modulo 4).
- [x] `teoria/06_reti_neurali.md` — neurone, attivazioni, backpropagation, epoche, batch (Modulo 5).

## 6. Stato di avanzamento

Legenda: [x] fatto, [ ] da fare. Il dettaglio di ogni esercizio è nella sezione 7.

- [x] Modulo 0 — completato (4 esercizi)
- [ ] Modulo 1 — in corso (8 esercizi su 12 fatti; il 9° è pronto da svolgere)
- [ ] Modulo 2
- [ ] Modulo 3
- [ ] Modulo 4
- [ ] Modulo 5
- [ ] Modulo 6

**Ultima sessione: 2026-11-25.** **Prossimo passo:** `modulo1/09_file.py`
(lettura e scrittura di file con `open`, `with`, `Path`: voti salvati su file).

## 7. Catalogo degli esercizi

Per ogni esercizio: file, obiettivo, concetti nuovi ed eventuali note emerse durante lo
svolgimento. Gli esercizi segnati [x] sono già svolti e pubblicati; gli altri sono il piano
e possono essere adattati man mano. **Tutti i file degli esercizi sono già creati** (Moduli 1-6), ciascuno con in testa:
obiettivo, passi, risultati attesi verificati, concetti nuovi, istruzioni per controllare da soli il risultato (ssert),
errori tipici e bonus facoltativi. Non serve altro per svolgerli: si leggono da VS Code e si scrive il codice sotto la descrizione.

Librerie da installare quando servono (con .venv attivo):
- Modulo 2: `pip install numpy pandas matplotlib`  - Modulo 4: `pip install scikit-learn`  - Moduli 5-6: `pip install torch torchvision`

### Modulo 0 — Primi passi (completato)

- [x] `modulo0/01_ciao.py` — **Primo programma.**
  Obiettivo: stampare "Ciao, mondo!". Concetti: funzione `print`, stringa (testo tra virgolette),
  esecuzione di un file da VS Code.
- [x] `modulo0/02_input.py` — **Chiedere il nome e salutare.**
  Obiettivo: leggere il nome con `input` e salutare ("Ciao, Marco!"). Concetti: `input`,
  variabile (un nome a cui si assegna un valore), unire testo e variabile con `print`.
- [x] `modulo0/03_eta.py` — **Età tra 10 anni.**
  Obiettivo: chiedere nome ed età e stampare "Marco, tra 10 anni avrai 40 anni".
  Concetti: `input` restituisce sempre testo, conversione con `int()`, calcoli, **f-string**
  (`f"{nome} ... {eta + 10}"`: le graffe vengono sostituite con il valore calcolato).
- [x] `modulo0/04_calcolatrice.py` — **Mini calcolatrice.**
  Obiettivo: chiedere due numeri e stampare somma, differenza, prodotto, divisione e,
  come extra, divisione intera, resto e potenza. Concetti: `float()`, operatori
  `+ - * / // % **`. Osservato: dividere per zero dà `ZeroDivisionError`; il programma si
  ferma alla riga dell'errore, le righe precedenti sono già state stampate.

### Modulo 1 — Python base (in corso)

- [x] `modulo1/01_condizioni.py` — **Positivo, negativo o zero.**
  Obiettivo: dire se un numero è positivo, negativo o zero; extra: maggiorenne/minorenne.
  Concetti: confronti (`> < >= <= == !=`), `if / elif / else`, indentazione di 4 spazi,
  differenza tra `=` (assegnazione) e `==` (confronto). Attenzione al caso limite 18 (`>=`).
- [x] `modulo1/02_cicli.py` — **Tabellina con il ciclo for.**
  Obiettivo: stampare la tabellina di un numero, con limite scelto dall'utente (default 10 se
  si preme Invio) e, come extra, la somma dei numeri da 1 a 100 (risultato 5050).
  Concetti: `for`, `range(inizio, fine)` con fine **escluso**, variabile **accumulatore**
  (`totale = totale + i`) che parte da 0 prima del ciclo e si aggiorna a ogni giro.
- [x] `modulo1/03_liste.py` — **Voti e media.**
  Obiettivo: chiedere 5 voti, salvarli in una lista e stampare lista, massimo, minimo e media.
  Concetti: lista (`[]`), `append`, indici che partono da 0, `len`, `max`, `min`, `sum`,
  media = `sum / len`. Errore incontrato e corretto: `range(6)` ripete 6 volte, non 5;
  per N giri si scrive `range(N)`.
- [x] `modulo1/04_dizionari.py` — **Rubrica.**
  Obiettivo: rubrica nome → numero con 3 contatti iniziali; cercare un nome (controllando con
  `in`), aggiungere un contatto, stampare tutta la rubrica. Concetti: dizionario `{chiave: valore}`,
  lettura per chiave, `in`, `.items()`, `KeyError`, numero di telefono come testo (zero iniziale).
  Extra: `.get("Nome", "non trovato")` e `len(rubrica)`.
- [x] `modulo1/05_funzioni.py` — **Funzioni.**
  Obiettivo: scrivere funzioni `media(lista)`, `e_pari(n)`, `massimo_di_tre(a, b, c)` e
  riscrivere l'esercizio dei voti usando le funzioni. Concetti: `def`, parametri, `return`,
  differenza tra stampare e restituire un valore, riuso del codice.
- [x] `modulo1/06_while_indovina.py` — **Indovina il numero.**
  Obiettivo: il programma sceglie un numero casuale tra 1 e 100; si prova finché si indovina,
  con indizi "più alto/più basso" e conteggio dei tentativi. Concetti: ciclo `while`,
  `break`, modulo `random` (`import`), confronti.
- [x] `modulo1/07_fizzbuzz.py` — **FizzBuzz.**
  Obiettivo: per i numeri da 1 a 100 stampare "Fizz" se multiplo di 3, "Buzz" se di 5,
  "FizzBuzz" se di entrambi, altrimenti il numero. Concetti: operatore `%`, ordine dei
  controlli in `if/elif`, condizioni combinate con `and`.
- [x] `modulo1/08_contaparole.py` — **Contatore di parole.**
  Obiettivo: dato un testo, contare quante volte compare ogni parola e stampare le 5 più
  frequenti. Concetti: metodi delle stringhe (`lower`, `split`), dizionario come contatore,
  ordinamento con `sorted` e `key`.
- [ ] `modulo1/09_file.py` — **Leggere e scrivere file.**
  Obiettivo: salvare dei voti in un file di testo, poi rileggerli e calcolare la media.
  Concetti: `open`, istruzione `with`, modalità `"w"`, `"a"`, `"r"`, `readlines`, percorsi
  relativi (nessun percorso assoluto nel codice).
- [ ] `modulo1/10_errori.py` — **Gestire gli errori.**
  Obiettivo: chiedere un numero e ripetere la domanda finché l'input è valido; gestire la
  divisione per zero. Concetti: `try / except`, `ValueError`, `ZeroDivisionError`, ciclo
  `while True` con `break`.
- [ ] `modulo1/11_convertitore.py` — **Convertitore di unità con menu.**
  Obiettivo: menu per convertire km↔miglia, °C↔°F, kg↔libbre. Concetti: funzioni,
  dizionario di conversioni, menu in un ciclo, gestione dell'input errato.
- [ ] `modulo1/12_riepilogo.py` — **Programma di fine modulo: registro voti.**
  Obiettivo: menu per aggiungere un voto, vedere la media per materia, salvare e caricare da
  file. Combina liste, dizionari, funzioni, file e `try/except`.

### Modulo 2 — Strumenti per i dati (da fare)

- [ ] `modulo2/01_numpy_array.py` — **Primi array.** Creare array con `np.array`, `arange`,
  `linspace`; `mean`, `std`, `min`, `max`; confronto con le liste. Concetti: array, tipo (`dtype`).
- [ ] `modulo2/02_numpy_vettori.py` — **Operazioni vettoriali.** Calcolare su tutto un array
  senza cicli (`a * 2`, `a + b`, `a ** 2`); condizioni (`a > 5`) e filtro con maschera.
  Concetti: vettorializzazione, perché è molto più veloce di un ciclo `for` (misura dei tempi).
- [ ] `modulo2/03_numpy_matrici.py` — **Matrici.** `shape`, `reshape`, indici e slicing,
  somma per righe/colonne (`axis`), trasposta, prodotto tra matrici (`@`).
  Concetti: matrice, dimensioni, il prodotto matriciale come base dei livelli di una rete.
- [ ] `modulo2/04_pandas_csv.py` — **Caricare un CSV.** `pd.read_csv`, `head`, `info`,
  `describe`, selezione di colonne. Concetti: DataFrame, Series, righe e colonne di una tabella.
- [ ] `modulo2/05_pandas_filtri.py` — **Filtri e raggruppamenti.** Filtrare righe con condizioni,
  ordinare, `groupby` con media e conteggio. Concetti: indicizzazione booleana, aggregazione.
- [ ] `modulo2/06_pandas_pulizia.py` — **Dati mancanti.** `isna`, `dropna`, `fillna`, duplicati,
  correzione di tipi. Concetti: perché i dati reali sono sporchi e come si prepara un dataset.
- [ ] `modulo2/07_matplotlib.py` — **Tre grafici.** Grafico a linee, istogramma, grafico a
  dispersione con titoli e assi etichettati. Concetti: figura e assi, quale grafico per quale dato.
- [ ] `modulo2/08_esplorazione.py` — **Mini analisi completa.** Scegliere un dataset pubblico,
  caricarlo, pulirlo, calcolare statistiche e produrre 3 grafici commentati.

### Modulo 3 — Regressione lineare a mano (da fare)

Solo NumPy. Teoria introdotta passo passo: campione, caratteristica (feature), etichetta (label),
modello, parametri, funzione di perdita, gradiente, learning rate.

- [ ] `modulo3/01_dati_retta.py` — **Dati su una retta.** Generare x, calcolare
  `y = 2x + 1` più rumore casuale e disegnarli. Concetti: campione, feature ed etichetta, rumore.
- [ ] `modulo3/02_modello.py` — **Il modello.** Funzione `predici(x, w, b)` con `y = w*x + b`;
  provare parametri a caso e disegnare la retta sui dati. Concetti: modello, parametri.
- [ ] `modulo3/03_perdita.py` — **Funzione di perdita.** Errore quadratico medio (MSE);
  calcolarlo per molti valori di `w` e disegnare perdita contro `w`. Concetti: perdita, minimo.
- [ ] `modulo3/04_derivata_numerica.py` — **Pendenza numerica.** Stimare di quanto cambia la
  perdita spostando `w` di un piccolo `epsilon`. Concetti: derivata come pendenza.
- [ ] `modulo3/05_gradiente.py` — **Gradiente.** Formule del gradiente di MSE rispetto a `w`
  e `b`; verifica contro il valore numerico. Concetti: gradiente, derivata parziale.
- [ ] `modulo3/06_un_passo.py` — **Un passo di gradient descent.** Aggiornare `w` e `b`
  nella direzione opposta al gradiente e verificare che la perdita scenda. Concetto: learning rate.
- [ ] `modulo3/07_training_loop.py` — **Addestramento completo.** Ripetere i passi per
  molte epoche, registrare la perdita e disegnarla. Concetti: epoca, addestramento, convergenza.
- [ ] `modulo3/08_learning_rate.py` — **Effetto del learning rate.** Provare valori troppo
  piccoli e troppo grandi; osservare lentezza e divergenza.
- [ ] `modulo3/09_confronto.py` — **Verifica.** Confrontare i parametri trovati con quelli di
  `np.polyfit`; discutere le differenze.

### Modulo 4 — Machine learning classico (da fare)

- [ ] `modulo4/01_iris_esplora.py` — **Esplorare Iris.** Caricare il dataset, osservare
  feature ed etichette, grafici per coppie di feature. Concetti: classificazione, classi.
- [ ] `modulo4/02_split.py` — **Train e test.** `train_test_split`; perché si valuta su dati
  mai visti. Concetti: training set, test set, `random_state`.
- [ ] `modulo4/03_regressione_logistica.py` — **Primo classificatore.** Addestrare, prevedere,
  calcolare l'accuratezza. Concetti: `fit`, `predict`, `score`, probabilità in uscita.
- [ ] `modulo4/04_albero.py` — **Albero decisionale.** Addestrare un albero, visualizzarlo,
  variare la profondità. Concetti: regole `if/else` apprese dai dati.
- [ ] `modulo4/05_overfitting.py` — **Overfitting.** Grafico di accuratezza su train e test al
  variare della complessità. Concetti: overfitting, underfitting, generalizzazione.
- [ ] `modulo4/06_metriche.py` — **Metriche.** Matrice di confusione, precisione, recall, F1 su
  un dataset sbilanciato; perché l'accuratezza da sola inganna.
- [ ] `modulo4/07_dataset_sporco.py` — **Dataset reale.** Valori mancanti, variabili
  categoriche, pipeline di preparazione e modello.
- [ ] `modulo4/08_confronto_modelli.py` — **Confronto.** Cross-validation su due o tre modelli
  e tabella dei risultati con commento.

### Modulo 5 — Reti neurali (da fare)

- [ ] `modulo5/01_neurone.py` — **Un neurone a mano.** Somma pesata degli ingressi più bias e
  funzione di attivazione. Concetti: peso, bias, attivazione.
- [ ] `modulo5/02_attivazioni.py` — **Funzioni di attivazione.** Sigmoide, ReLU, tanh:
  scriverle e disegnarle. Concetto: perché serve la non linearità.
- [ ] `modulo5/03_perceptron.py` — **Perceptron.** Imparare le porte AND e OR con la regola di
  aggiornamento dei pesi; vedere che XOR non si riesce con un solo neurone.
- [ ] `modulo5/04_xor_a_mano.py` — **Rete a due strati a mano.** Propagazione in avanti e
  **backpropagation** scritta con NumPy; la rete impara XOR. Concetti: strati, retropropagazione.
- [ ] `modulo5/05_tensori.py` — **Tensori in PyTorch.** Creazione, operazioni, forma, passaggio
  da NumPy a tensori e viceversa.
- [ ] `modulo5/06_autograd.py` — **Gradiente automatico.** `requires_grad`, `backward`;
  confronto con il gradiente calcolato a mano nel Modulo 3.
- [ ] `modulo5/07_xor_pytorch.py` — **XOR in PyTorch.** `nn.Module`, funzione di perdita,
  ottimizzatore, ciclo di training. Concetti: epoca, batch, ottimizzatore.
- [ ] `modulo5/08_confronto.py` — **A mano contro PyTorch.** Stessi dati, stessi risultati?
  Effetto di learning rate ed epoche.

### Modulo 6 — Primo progetto (da fare)

- [ ] `modulo6/01_dati_mnist.py` — **Dati MNIST.** Scaricare il dataset (la cartella `data/` non
  va nel repository), guardare alcune immagini, forma dei dati, normalizzazione.
- [ ] `modulo6/02_rete_base.py` — **Rete base.** Rete densa, ciclo di training con batch, curva
  della perdita.
- [ ] `modulo6/03_valutazione.py` — **Valutazione.** Accuratezza sul test set, matrice di
  confusione.
- [ ] `modulo6/04_errori.py` — **Analisi degli errori.** Mostrare le immagini sbagliate e capire
  perché; quali cifre vengono confuse.
- [ ] `modulo6/05_miglioramenti.py` — **Miglioramenti.** Più strati o neuroni, più epoche,
  dropout; confronto dei risultati.
- [ ] `modulo6/06_relazione.md` — **Relazione finale.** Descrizione del progetto, risultati,
  grafici e cosa è stato imparato.






