# Teoria 4 — Apprendere dai dati: regressione lineare e gradient descent

Il cuore del machine learning in un unico esempio completo. Quello che qui si fa con una retta
(due numeri da imparare) è **esattamente** quello che si fa con una rete neurale con milioni di
parametri: cambia solo la dimensione del problema.

Serve per gli esercizi `modulo3/01` … `modulo3/09`. Prerequisiti: `03_numpy_pandas.md`
(array, operazioni vettoriali, grafici).

Indice: [1. Cos'è il machine learning](#1-cosè-il-machine-learning) ·
[2. Vocabolario](#2-vocabolario) · [3. Il modello lineare](#3-il-modello-lineare) ·
[4. La funzione di perdita](#4-la-funzione-di-perdita) ·
[5. Derivate in poche righe](#5-derivate-in-poche-righe) · [6. Il gradiente della perdita](#6-il-gradiente-della-perdita) ·
[7. Gradient descent](#7-gradient-descent) · [8. Learning rate](#8-learning-rate) ·
[9. Epoche e batch](#9-epoche-e-batch) · [10. Più caratteristiche (forma matriciale)](#10-più-caratteristiche-forma-matriciale) ·
[11. Valutare il modello](#11-valutare-il-modello) · [12. Errori frequenti e controlli](#12-errori-frequenti-e-controlli)

---

## 1. Cos'è il machine learning

**Programmazione tradizionale:** scrivi tu le regole. "Se la temperatura è sopra 30, stampa *caldo*."

**Machine learning:** fornisci **esempi** (dati con la risposta giusta) e un programma
**ricava le regole da solo**. Invece di scrivere "il prezzo di una casa è 3000 € al metro quadro",
mostri mille case con superficie e prezzo, e il programma scopre il rapporto.

Le grandi famiglie:

- **Apprendimento supervisionato:** gli esempi hanno la risposta giusta (etichetta).
  - **Regressione:** la risposta è un **numero** (prezzo, temperatura, altezza).
  - **Classificazione:** la risposta è una **categoria** (cifra 0–9, spam/non spam).
- **Apprendimento non supervisionato:** nessuna risposta; si cercano strutture (gruppi, anomalie).
- **Apprendimento per rinforzo:** un agente impara per tentativi, con premi e penalità.

In questo corso ci occupiamo di apprendimento supervisionato. Questo capitolo: regressione.

## 2. Vocabolario

Termini che userai per tutto il corso (tra parentesi il nome inglese, che troverai ovunque):

| Termine | Significato | Esempio |
|---|---|---|
| **Campione** (*sample*, *example*) | una riga di dati | una casa |
| **Caratteristica** (*feature*) | un valore in ingresso che descrive il campione | superficie = 80 m² |
| **Etichetta** (*label*, *target*) | la risposta giusta che vogliamo prevedere | prezzo = 240 000 € |
| **Dataset** | l'insieme dei campioni | 1000 case |
| **Modello** | una funzione che trasforma le feature in una previsione | `prezzo = w·superficie + b` |
| **Parametri** (*parameters*, *weights*) | i numeri nel modello che vengono imparati | `w` e `b` |
| **Iperparametri** | impostazioni che scegli tu e non vengono imparate | learning rate, numero di epoche |
| **Previsione** (*prediction*) | l'uscita del modello per un campione | ŷ (si legge "y cappello") |
| **Perdita** (*loss*) | numero che misura quanto il modello sbaglia | errore quadratico medio |
| **Addestramento** (*training*) | il processo che regola i parametri per ridurre la perdita | gradient descent |

Notazione: *x* = caratteristica, *y* = etichetta vera, *ŷ* = previsione del modello, *N* = numero
di campioni, *xᵢ* e *yᵢ* = l'*i*-esimo campione.

## 3. Il modello lineare

Il modello più semplice con una sola feature è una **retta**:

```
ŷ = w · x + b
```

- **w** (peso, *weight*): la **pendenza**. Di quanto cambia ŷ quando x aumenta di 1.
- **b** (*bias*): l'**intercetta**. Il valore di ŷ quando x = 0.

I due numeri sono i **parametri**. Cambiare *w* e *b* cambia la retta. **Imparare = trovare i
valori di *w* e *b* per cui la retta passa "bene" in mezzo ai dati.**

In Python, con NumPy, per tutti i campioni in una volta:

```python
def predici(x, w, b):
    return w * x + b
```

I dati reali non stanno mai esattamente su una retta: c'è **rumore** (errori di misura, fattori
non considerati). Per esercitarci generiamo dati con una retta vera più rumore:

```python
rng = np.random.default_rng(42)
x = rng.uniform(0, 10, 50)
y = 2 * x + 1 + rng.normal(0, 1.5, 50)     # retta vera: w = 2, b = 1, rumore con dev. std. 1.5
```

Il modello non conosce i valori veri (2 e 1): deve **ricavarli dai dati**.

## 4. La funzione di perdita

Per dire "questa retta è meglio di quella" serve un **numero** che misuri l'errore.

**Errore** per un campione: `eᵢ = ŷᵢ − yᵢ` (previsione meno valore vero).

Non si usa la somma degli errori, perché errori positivi e negativi si cancellerebbero.
Si usa l'**errore quadratico medio** (MSE, *Mean Squared Error*):

```
L(w, b) = (1/N) · Σ (w·xᵢ + b − yᵢ)²
```

Cioè: per ogni campione calcola l'errore, **eleva al quadrato**, poi fai la **media**.

```python
def mse(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)
```

Perché il quadrato:
- rende ogni errore positivo (nessuna cancellazione);
- penalizza **molto di più** gli errori grandi (un errore di 4 pesa 16, due errori di 2 pesano 8);
- è una funzione **liscia** e derivabile ovunque, requisito per il passo successivo.

Alternativa: **MAE** (errore assoluto medio), `mean(|e|)`, meno sensibile agli outlier ma non
derivabile in 0.

**Esempio numerico.** Dati `x = [1, 2, 3]`, `y = [2, 4, 6]`, parametri `w = 0`, `b = 0`:

```
previsioni:  ŷ = [0, 0, 0]
errori:      e = ŷ − y = [−2, −4, −6]
quadrati:    [4, 16, 36]
MSE:         (4 + 16 + 36) / 3 = 18.667
```

Con i parametri giusti (`w = 2`, `b = 0`) la perdita sarebbe 0. **Addestrare significa cercare i
parametri che rendono la perdita il più piccola possibile.**

La perdita è una funzione dei **parametri** (non dei dati, che sono fissi): `L(w, b)`.
Immaginala come un paesaggio: ogni coppia (w, b) è un punto sul terreno e la perdita è la
**quota**. Vogliamo arrivare al fondo della valle.

## 5. Derivate in poche righe

Come scendere in una valle senza vederla? Si sente **da che parte il terreno scende** sotto i piedi.
La matematica di questa sensazione è la **derivata**.

**Idea.** La derivata di una funzione *f* in un punto è la sua **pendenza** lì:
di quanto cambia *f* se si sposta un po' l'ingresso.

- derivata **positiva**: la funzione sta salendo (andando verso destra);
- derivata **negativa**: sta scendendo;
- derivata **zero**: punto piatto (minimo, massimo o sella).

**Definizione intuitiva** (derivata numerica):

```
f'(x) ≈ ( f(x + ε) − f(x − ε) ) / (2ε)     con ε molto piccolo, ad es. 1e-5
```

In codice:

```python
def derivata(f, x, eps=1e-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps)

derivata(lambda t: t ** 2, 3)       # circa 6
```

**Regole che servono (e basta):**

| Funzione | Derivata |
|---|---|
| costante `c` | `0` |
| `x` | `1` |
| `a·x` | `a` |
| `x²` | `2x` |
| somma `f + g` | `f' + g'` |
| costante per funzione `c·f` | `c·f'` |
| **catena** `f(g(x))` | `f'(g(x)) · g'(x)` |

La **regola della catena** è quella che userai di più (e che è alla base della
backpropagation): per una funzione "dentro un'altra", derivi quella esterna e moltiplichi per
la derivata di quella interna. Esempio: `(3x + 1)²` ha derivata `2·(3x + 1)·3`.

**Derivate parziali.** Quando la funzione ha **più ingressi** (qui *w* e *b*), si deriva
rispetto a uno alla volta tenendo gli altri fissi. Si scrive ∂L/∂w e ∂L/∂b.
La derivata parziale dice: "se muovo solo *w* di un pelo, di quanto cambia la perdita?"

**Gradiente.** È il vettore di tutte le derivate parziali: `∇L = (∂L/∂w, ∂L/∂b)`.
Punta nella direzione in cui la perdita **sale più rapidamente**. Quindi la direzione
**opposta** è quella in cui scende più rapidamente.

## 6. Il gradiente della perdita

Calcoliamo le derivate di `L(w, b) = (1/N) Σ (w·xᵢ + b − yᵢ)²`.

Indichiamo con `eᵢ = w·xᵢ + b − yᵢ` l'errore del campione *i*. Allora `L = (1/N) Σ eᵢ²`.

Per la regola della catena (esterna: quadrato; interna: l'errore):

```
∂(eᵢ²)/∂w = 2·eᵢ · ∂eᵢ/∂w = 2·eᵢ · xᵢ      (perché ∂eᵢ/∂w = xᵢ)
∂(eᵢ²)/∂b = 2·eᵢ · ∂eᵢ/∂b = 2·eᵢ · 1       (perché ∂eᵢ/∂b = 1)
```

Mediando su tutti i campioni:

```
∂L/∂w = (2/N) · Σ eᵢ · xᵢ
∂L/∂b = (2/N) · Σ eᵢ
```

In NumPy:

```python
def gradiente(x, y, w, b):
    e = w * x + b - y                  # errori, vettore di N elementi
    dw = 2 * np.mean(e * x)
    db = 2 * np.mean(e)
    return dw, db
```

**Esempio numerico** (stessi dati di prima, `w = 0`, `b = 0`): errori `e = [−2, −4, −6]`.

```
∂L/∂w = (2/3) · (−2·1 + −4·2 + −6·3) = (2/3) · (−28) = −18.667
∂L/∂b = (2/3) · (−2 − 4 − 6)         = (2/3) · (−12) = −8.0
```

Entrambe negative: aumentando *w* e *b* la perdita **scende**. È coerente: la retta vera ha
pendenza 2 e noi partiamo da 0.

**Controllo con la derivata numerica:** `(L(w+ε, b) − L(w−ε, b)) / (2ε)` deve coincidere
con `∂L/∂w` a 4–5 cifre. È **il** modo per scoprire errori nelle formule: se non coincide,
una delle due è sbagliata.

## 7. Gradient descent

Idea: **partire da parametri qualsiasi e fare piccoli passi nella direzione opposta al gradiente**,
cioè in discesa, ripetutamente.

```
w ← w − η · ∂L/∂w
b ← b − η · ∂L/∂b
```

Il simbolo `←` significa "diventa". **η** (eta, spesso scritto `lr` nel codice) è il
**learning rate**: la lunghezza del passo.

Algoritmo:

```
1. scegli w, b iniziali (ad es. 0)
2. ripeti per molte epoche:
     a. calcola la previsione ŷ = w·x + b per tutti i campioni
     b. calcola la perdita L (per monitorarla)
     c. calcola il gradiente (dw, db)
     d. aggiorna:  w = w − lr·dw ;  b = b − lr·db
3. alla fine w e b sono i parametri "imparati"
```

In codice:

```python
w, b = 0.0, 0.0
lr = 0.01
storia = []
for epoca in range(1000):
    dw, db = gradiente(x, y, w, b)
    w = w - lr * dw
    b = b - lr * db
    storia.append(mse(predici(x, w, b), y))
```

**Esempio numerico completo** (dati `x = [1, 2, 3]`, `y = [2, 4, 6]`, `lr = 0.1`):

```
Passo 0:  w = 0,      b = 0       perdita 18.667   gradiente (−18.667, −8.0)
Passo 1:  w = 0 − 0.1·(−18.667) = 1.867      b = 0 − 0.1·(−8.0) = 0.8
          previsioni [2.667, 4.533, 6.4]    perdita 0.296
          gradiente (≈ 1.956 , ≈ 1.067)  (ora i gradienti sono positivi: abbiamo "superato" un po')
Passo 2:  w = 1.867 − 0.1·1.956 = 1.671     b = 0.8 − 0.1·1.067 = 0.693
          perdita 0.073
```

La perdita passa da 18.667 a 0.296 a 0.073: **sta scendendo**. Ripetendo il processo
converge verso la soluzione. Questa è l'**addestramento**.

Proprietà importanti:
- Con una perdita "a ciotola" come l'MSE della regressione lineare, il gradient descent trova
  l'**unico minimo**. Per le reti neurali il paesaggio è molto più accidentato e si trovano
  buoni minimi locali, non necessariamente il migliore.
- Il gradiente diventa piccolo vicino al minimo: i passi si accorciano da soli e il processo
  rallenta; non serve fermarsi a un numero preciso di epoche, ma quando la perdita non scende più.
- L'algoritmo non "sa" la soluzione: vede solo la pendenza nel punto in cui si trova.

## 8. Learning rate

Il learning rate **η** è l'iperparametro più importante.

- **Troppo piccolo:** i passi sono minuscoli, ci vogliono moltissime epoche (si addestra "a rilento").
- **Giusto:** la perdita scende rapidamente e poi si stabilizza.
- **Troppo grande:** si "salta" al di là della valle, ogni passo peggiora, la perdita cresce
  sempre più veloce fino a numeri enormi (`inf`, `nan`). Si dice che l'addestramento **diverge**.

Nel dataset degli esercizi (50 punti con x tra 0 e 10), con `lr = 0.01` la perdita converge,
con `lr = 0.02` converge più in fretta, con `lr = 0.03` o più **diverge**. La soglia dipende
dalla "ripidità" della valle (la derivata seconda), che qui è legata a `mean(x²)`: le feature
con valori grandi rendono la valle ripida e richiedono learning rate piccoli.

**Normalizzazione delle feature.** Se *x* vale da 0 a 10 000, la valle è molto ripida
in una direzione e piatta nell'altra: serve un learning rate minuscolo e l'addestramento è lento.
Si risolve **standardizzando** le feature: `x_norm = (x − media) / deviazione standard`.
Dopo la standardizzazione si possono usare learning rate molto più grandi (0.1 o più).
È una delle pratiche più importanti, e vale anche per le reti neurali.

**Come scegliere:** si prova una sequenza (0.001, 0.01, 0.1, …), si disegna la curva della
perdita e si sceglie il valore più grande che non diverge.

## 9. Epoche e batch

- **Epoca** (*epoch*): un passaggio completo su **tutto** il dataset. Nell'esempio sopra ogni
  iterazione usa tutti i campioni, quindi 1 iterazione = 1 epoca.
- **Full-batch gradient descent:** il gradiente è calcolato su **tutti** i campioni a ogni passo
  (quello che facciamo noi). Preciso ma lento con dataset enormi.
- **Stochastic gradient descent (SGD):** il gradiente è calcolato su **un solo** campione per
  volta. Veloce ma molto "rumoroso".
- **Mini-batch:** compromesso: si usano gruppi (*batch*) di, ad esempio, 32 o 64 campioni.
  È lo standard per le reti neurali. Un'epoca = tanti passi quanti sono i batch
  (dataset da 60 000 campioni con batch da 64 → 938 passi per epoca).

Termini: **batch size** (quanti campioni per passo), **epoche** (quante volte si scorre il dataset),
**iterazione/passo** (un singolo aggiornamento dei parametri).

## 10. Più caratteristiche (forma matriciale)

Con più feature (superficie, stanze, età) il modello diventa:

```
ŷ = w₁·x₁ + w₂·x₂ + … + w_d·x_d + b
```

In forma compatta con vettori e matrici: la matrice dei dati **X** ha forma `(N, d)`
(una riga per campione), i pesi **w** hanno forma `(d,)`:

```
ŷ = X @ w + b          # vettore di N previsioni
e = ŷ − y              # N errori
L = mean(e²)
∂L/∂w = (2/N) · Xᵀ @ e       # vettore di d derivate, una per peso
∂L/∂b = (2/N) · sum(e)
```

È la **stessa** formula di prima, scritta per tutte le feature in una volta. In codice:

```python
def gradiente(X, y, w, b):
    e = X @ w + b - y
    dw = 2 * (X.T @ e) / len(y)
    db = 2 * np.mean(e)
    return dw, db
```

Controllo delle forme: `X.T` è `(d, N)`, `e` è `(N,)` → `X.T @ e` è `(d,)`. Come `w`. ✔

Questo è già un **neurone lineare**: nel Modulo 5 aggiungeremo una funzione non lineare e
impileremo più strati.

## 11. Valutare il modello

- **Curva della perdita:** grafico perdita contro epoca. Deve scendere e poi appiattirsi.
  Se sale: learning rate troppo alto o errore nel gradiente. Se scende lentissima: learning rate
  troppo basso.
- **Confronto con la soluzione esatta:** per la regressione lineare esiste una formula chiusa
  (minimi quadrati): `w = cov(x, y) / var(x)`, `b = mean(y) − w·mean(x)`. `np.polyfit(x, y, 1)`
  la calcola. Il gradient descent, ben addestrato, deve arrivare agli **stessi valori**.
- **R²** (coefficiente di determinazione): `1 − SS_res / SS_tot`, con
  `SS_res = Σ(yᵢ − ŷᵢ)²` e `SS_tot = Σ(yᵢ − media(y))²`. Vale 1 se il modello è perfetto, 0 se è
  buono quanto "prevedere sempre la media", negativo se peggiore.
- **Importante:** una perdita bassa **sui dati di addestramento** non basta. Si valuta su dati
  **non visti** (train/test, Modulo 4). Con un modello semplice come una retta il rischio
  è basso; con modelli complessi è il problema principale (*overfitting*).

## 12. Errori frequenti e controlli

| Sintomo | Causa probabile |
|---|---|
| La perdita **cresce** a ogni epoca | learning rate troppo grande; oppure segno sbagliato nell'aggiornamento (`+` invece di `−`) |
| La perdita diventa `nan` o `inf` | divergenza (learning rate troppo grande) |
| La perdita **non cambia** | learning rate troppo piccolo; gradiente calcolato male (sempre 0); parametri non aggiornati |
| `w` converge, `b` molto più lento | normale se le feature hanno scale diverse: standardizza x |
| Il gradiente non coincide con quello numerico | errore di formula: ricontrolla `e * x` contro `e` |
| Previsioni con la forma sbagliata | errori di broadcasting: controlla `.shape` di ogni array |

**Checklist prima di fidarsi dell'addestramento:**
1. Il gradiente analitico coincide con quello numerico (esercizio 05).
2. Un singolo passo riduce la perdita (esercizio 06).
3. La curva della perdita decresce senza salti (esercizio 07).
4. I parametri finali sono vicini a quelli di `np.polyfit` (esercizio 09).

Ricorda l'immagine di fondo: **modello → perdita → gradiente → piccolo passo → ripeti**.
Tutto il deep learning è questo ciclo, con modelli più grandi e gradienti calcolati
automaticamente (backpropagation).
