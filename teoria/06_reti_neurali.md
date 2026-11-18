# Teoria 6 — Reti neurali e PyTorch

Dal neurone singolo alla backpropagation, fino a un ciclo di addestramento completo in PyTorch.
Serve per gli esercizi `modulo5/01` … `modulo5/08` e per il progetto del Modulo 6.
Prerequisiti: `04_regressione_gradient_descent.md` (gradient descent, perdita) e
`05_ml_classico.md` (train/test, cross-entropy, overfitting).

**Installazione** (CPU, sufficiente per tutto il corso; circa 200 MB):

```powershell
pip install torch torchvision
```

Indice: [1. Il neurone artificiale](#1-il-neurone-artificiale) ·
[2. Funzioni di attivazione](#2-funzioni-di-attivazione) · [3. Strati e matrici](#3-strati-e-matrici) ·
[4. Propagazione in avanti e perdita](#4-propagazione-in-avanti-e-perdita) ·
[5. Backpropagation](#5-backpropagation) · [6. Addestrare una rete](#6-addestrare-una-rete) ·
[7. Il perceptron e il problema XOR](#7-il-perceptron-e-il-problema-xor) ·
[8. Overfitting nelle reti](#8-overfitting-nelle-reti) · [9. PyTorch](#9-pytorch) ·
[10. Errori comuni](#10-errori-comuni)

---

## 1. Il neurone artificiale

Un **neurone** è la stessa cosa del modello lineare del Modulo 3, più un passo in più:

```
z = w₁·x₁ + w₂·x₂ + … + w_d·x_d + b      (somma pesata degli ingressi più il bias)
a = f(z)                                  (funzione di attivazione)
```

- **x**: gli ingressi (feature, o uscite dei neuroni precedenti).
- **w**: i **pesi**: quanto conta ciascun ingresso (parametri da imparare).
- **b**: il **bias**: una soglia regolabile.
- **f**: la **funzione di attivazione**: introduce **non linearità**.
- **a**: l'uscita (*attivazione*) del neurone.

Con vettori: `z = w @ x + b`.

**Esempio numerico.** `x = [2, 3]`, `w = [0.4, −0.2]`, `b = 0.5`:
`z = 0.4·2 + (−0.2)·3 + 0.5 = 0.8 − 0.6 + 0.5 = 0.7`. Con la sigmoide: `a = 1/(1+e^−0.7) ≈ 0.668`.

Il nome richiama i neuroni biologici (molti ingressi, un'uscita, "si accende" sopra una soglia), ma
l'analogia finisce lì: una rete neurale è semplicemente una **funzione matematica composta**, con
parametri regolabili.

## 2. Funzioni di attivazione

Senza attivazione, un neurone è lineare, e **una composizione di funzioni lineari è ancora una
funzione lineare**: una rete con 100 strati lineari sarebbe equivalente a un solo strato. L'attivazione
**non lineare** è ciò che permette alla rete di rappresentare funzioni complesse.

| Nome | Formula | Uscita | Uso |
|---|---|---|---|
| **Sigmoide** | `1 / (1 + e^−z)` | tra 0 e 1 | probabilità (uscita binaria), vecchi strati nascosti |
| **Tanh** | `(e^z − e^−z)/(e^z + e^−z)` | tra −1 e 1 | strati nascosti (centrata in zero) |
| **ReLU** | `max(0, z)` | da 0 a +∞ | **standard** negli strati nascosti |
| **Softmax** | `e^zᵢ / Σ e^zⱼ` | per un vettore: numeri positivi che sommano 1 | uscita multiclasse (probabilità) |

Valori utili: `sigmoide(0) = 0.5`, `sigmoide(2) = 0.881`, `sigmoide(−2) = 0.119`;
`tanh(2) = 0.964`; `softmax([1, 2, 3]) = [0.090, 0.245, 0.665]`.

**Derivate** (servono per la backpropagation):
- sigmoide: `s'(z) = s(z)·(1 − s(z))`; massimo 0.25 in z = 0;
- tanh: `1 − tanh(z)²`;
- ReLU: `1` se z > 0, altrimenti `0`.

**Gradienti che svaniscono (vanishing gradient).** Per |z| grande la sigmoide è piatta: la sua derivata
è quasi 0 (per z = 10 vale 4.5·10⁻⁵). Nelle reti profonde i gradienti, moltiplicati strato dopo
strato, diventano minuscoli e l'addestramento si blocca. La **ReLU** ha derivata 1 per z > 0 e
risolve in gran parte il problema: per questo è lo standard.

**Softmax e stabilità numerica.** `e^z` esplode per z grandi (`e^1000` = inf). Si sottrae il massimo
prima: `softmax(z) = softmax(z − max(z))` (stesso risultato, nessun overflow).

## 3. Strati e matrici

Una **rete** organizza molti neuroni in **strati** (*layers*): lo **strato di ingresso** (i dati), uno o
più **strati nascosti**, lo **strato di uscita**. Ogni neurone di uno strato riceve **tutte** le uscite
dello strato precedente (strato *completamente connesso*, o *denso*, o *lineare*).

Tutti i neuroni di uno strato si calcolano **in un colpo solo** con un prodotto matriciale (teoria 03,
sezione 4):

```
Z = X @ W + b          X: (N, d_in)   W: (d_in, d_out)   b: (d_out,)   Z: (N, d_out)
A = f(Z)
```

- Una riga per campione, una colonna per neurone.
- **Numero di parametri** di uno strato: `d_in · d_out + d_out` (pesi più bias).
  Esempio: una rete 784 → 128 → 10 (immagini 28×28 di cifre) ha
  `784·128 + 128 + 128·10 + 10 = 101 770` parametri.

Rete a due strati (un nascosto):

```
H = f(X @ W1 + b1)          strato nascosto
Y = g(H @ W2 + b2)          uscita (g: sigmoide, softmax, o nessuna)
```

La rete è "profonda" (*deep*) quando ha molti strati nascosti: da qui *deep learning*.

**Inizializzazione dei pesi.** Mai tutti a zero: tutti i neuroni di uno strato farebbero la stessa
cosa e riceverebbero gli stessi gradienti (**simmetria**) e non si differenzierebbero mai. Si
inizializzano con piccoli numeri casuali (es. `rng.normal(0, 1, ...)` per reti piccole; PyTorch usa già
schemi adatti). I bias invece possono partire da zero.

## 4. Propagazione in avanti e perdita

**Forward pass** (propagazione in avanti): dai dati all'uscita, strato dopo strato, calcolando le
attivazioni. È la "previsione".

**Perdita** (la misura dell'errore, come nel Modulo 3):
- **Regressione:** errore quadratico medio (MSE).
- **Classificazione binaria:** cross-entropy binaria con uscita sigmoide.
- **Classificazione multiclasse:** cross-entropy con uscita softmax:
  `L = −(1/N) Σ log( p_classe_vera )`. Se la rete dà alla classe giusta probabilità 0.9, il
  contributo è −log 0.9 = 0.105; se 0.1, è 2.3.

**Esempio numerico completo** (un solo neurone sigmoide, una sola feature, MSE):
`x = 1`, `w = 0.5`, `b = 0`, valore vero `y = 1`:
`z = 0.5`, `a = σ(0.5) = 0.6225`, `L = (a − y)² = (0.6225 − 1)² = 0.1425`.

## 5. Backpropagation

L'addestramento usa il **gradient descent** (teoria 04): servono le derivate della perdita rispetto a
**tutti** i parametri. In una rete ce ne sono migliaia o milioni. La **backpropagation**
(*retropropagazione*) le calcola tutte in modo efficiente applicando la **regola della catena**
**all'indietro**, dall'uscita verso l'ingresso.

Idea: la perdita dipende dai pesi attraverso una catena di passaggi (peso → z → a → … → perdita).
La derivata della perdita rispetto a un peso è il **prodotto delle derivate lungo la catena**.

**Esempio completo, un neurone** (stessi numeri di prima):

```
L = (a − y)²          dL/da = 2(a − y)            = 2·(−0.3775) = −0.755
a = σ(z)              da/dz = a(1 − a)            = 0.6225·0.3775 = 0.2350
z = w·x + b           dz/dw = x = 1               dz/db = 1

dL/dw = dL/da · da/dz · dz/dw = −0.755 · 0.2350 · 1 = −0.1774
dL/db = −0.755 · 0.2350 · 1                          = −0.1774
```

Il segno negativo dice: aumentare *w* riduce la perdita. Aggiornando `w ← w − η·dL/dw` il
neurone si avvicina al valore vero.

**Rete a due strati** (sigmoide in entrambi gli strati, MSE), con `δ` = "errore propagato":

```
Forward:
  H = σ(X @ W1 + b1)
  Ŷ = σ(H @ W2 + b2)
  L = mean((Ŷ − Y)²)

Backward (dall'uscita all'ingresso):
  δ2 = (2/N) · (Ŷ − Y) · Ŷ · (1 − Ŷ)            forma (N, d_out)
  dW2 = Hᵀ @ δ2          db2 = somma di δ2 sulle righe
  δ1 = (δ2 @ W2ᵀ) · H · (1 − H)                  forma (N, d_hidden): l'errore "torna indietro" attraverso W2
  dW1 = Xᵀ @ δ1          db1 = somma di δ1 sulle righe
```

Schema mentale: **ogni strato riceve l'errore dallo strato dopo, lo moltiplica per la derivata
della propria attivazione, e lo passa allo strato prima**. I gradienti dei pesi si ottengono
combinando l'errore dello strato con l'ingresso di quello strato (`Hᵀ @ δ2`, `Xᵀ @ δ1`).

**Il controllo (gradient check):** la derivata numerica `(L(w+ε) − L(w−ε))/(2ε)` di un peso deve
coincidere con quella calcolata con la backpropagation. È il modo per scoprire errori di formula
(come nel Modulo 3).

**Differenziazione automatica.** Nessuno scrive a mano la backpropagation per reti reali: librerie
come PyTorch costruiscono un **grafo computazionale** durante il forward e calcolano tutti i gradienti
con una sola chiamata (`loss.backward()`). Capirla a mano una volta serve per capire cosa succede
dentro e per riconoscere i problemi (gradienti che svaniscono o esplodono).

## 6. Addestrare una rete

Il ciclo è lo stesso del Modulo 3:

```
per ogni epoca:
    per ogni mini-batch di campioni:
        1. forward: calcola le previsioni
        2. perdita: calcola L
        3. backward: calcola i gradienti
        4. aggiorna i parametri (passo dell'ottimizzatore)
```

Termini (vedi anche teoria 04, sezione 9):
- **Epoca**: un passaggio completo su tutto il training set.
- **Batch / mini-batch**: gruppo di campioni usato per un singolo aggiornamento (es. 64).
- **Iterazione (passo)**: un singolo aggiornamento. Con 60 000 campioni e batch 64: 938 passi per epoca.

**Ottimizzatori.** Regolano *come* usare il gradiente per aggiornare i pesi:
- **SGD** (*stochastic gradient descent*): `w ← w − η·g`, il metodo base.
- **SGD con momentum**: tiene memoria delle direzioni precedenti, smorza le oscillazioni.
- **Adam**: adatta il passo per ogni parametro; funziona bene con `lr = 0.001` di default; è la scelta
  standard di partenza.

**Learning rate:** come nel Modulo 3, è l'iperparametro più importante. Troppo alto: la perdita
oscilla o diverge; troppo basso: lentezza.

**Normalizzare gli ingressi** (media 0, deviazione standard 1): come in teoria 04, accelera e
stabilizza l'addestramento (per le immagini si usano la media e la deviazione standard del dataset).

## 7. Il perceptron e il problema XOR

Il **perceptron** è un singolo neurone con attivazione a gradino: uscita 1 se `z > 0`, altrimenti 0.
**Regola di apprendimento** (per ogni campione, `e = target − previsione`):

```
w ← w + η · e · x
b ← b + η · e
```

Se la previsione è giusta (`e = 0`) non cambia nulla; se è sbagliata, i pesi si spostano per
correggere l'errore.

Funziona per le porte logiche **AND** e **OR**: i punti delle due classi si possono separare con
**una retta**. Ma **non** per **XOR** (uscita 1 solo se gli ingressi sono diversi):

```
x1 x2 | AND OR XOR
 0  0 |  0   0   0
 0  1 |  0   1   1
 1  0 |  0   1   1
 1  1 |  1   1   0
```

I punti di XOR **non sono separabili da una retta** (provare a disegnarli: le due classi stanno agli
angoli opposti di un quadrato). Un singolo neurone — un modello lineare — non può impararla,
qualunque sia l'addestramento. Questo limite (1969) bloccò la ricerca per anni.

**Soluzione:** uno **strato nascosto**. Con due o più neuroni nascosti con attivazione non lineare la
rete costruisce una rappresentazione intermedia in cui le classi diventano separabili. È un esempio
concreto di perché servono **strati multipli e non linearità**.

## 8. Overfitting nelle reti

Le reti hanno moltissimi parametri e possono **memorizzare** il training set (teoria 05, sezione 6).
Strumenti:

- **Validation set** e **curve di apprendimento**: si disegnano perdita e accuratezza di train e
  validazione per epoca. Se la validazione peggiora mentre il training migliora: overfitting.
- **Early stopping**: fermare l'addestramento all'epoca in cui la validazione è migliore.
- **Dropout**: durante l'addestramento si "spengono" a caso alcuni neuroni (es. il 20%), così la rete
  non si affida a singoli neuroni. Si disattiva in valutazione (`model.eval()`).
- **Weight decay** (regolarizzazione L2): penalizza i pesi grandi.
- **Più dati / data augmentation**: ad esempio piccole rotazioni o traslazioni delle immagini.
- **Rete più piccola.**

## 9. PyTorch

PyTorch è la libreria che automatizza la maggior parte di questo lavoro.

### Tensori

Un **tensore** è un array multidimensionale (come NumPy) che può vivere su CPU o GPU e **tiene traccia
delle operazioni per calcolare i gradienti**.

```python
import torch
a = torch.tensor([1.0, 2.0, 3.0])      # creare da lista
b = torch.zeros(2, 3)                   # forma (2, 3)
a * 2;  a + a;  a @ a                   # stesse operazioni di NumPy
a.shape;  a.dtype                       # forma e tipo (float32 di default)
n = a.numpy()                           # → array NumPy
t = torch.from_numpy(n)                 # array NumPy → tensore (condividono la memoria)
x = torch.tensor(x_numpy, dtype=torch.float32)    # conversione esplicita
```

### Autograd (gradienti automatici)

```python
w = torch.tensor(2.0, requires_grad=True)       # "tieni traccia" di questo valore
y = w ** 2 + 3 * w                              # funzione: y = w² + 3w
y.backward()                                    # calcola dy/dw con la regola della catena
w.grad                                          # tensor(7.) : 2w + 3 = 7
```

- `requires_grad=True` dice a PyTorch di calcolare il gradiente rispetto a quel tensore.
- `backward()` calcola il gradiente di una quantità **scalare** (la perdita).
- I gradienti si **accumulano** in `.grad` a ogni `backward()`: vanno azzerati a ogni passo
  (`optimizer.zero_grad()` o `w.grad.zero_()`).
- `with torch.no_grad():` disattiva il tracciamento (per valutazione e per aggiornamenti manuali).
- `.item()` converte un tensore scalare in un numero Python; `.detach()` lo stacca dal grafo.

### Costruire una rete

```python
import torch.nn as nn

rete = nn.Sequential(
    nn.Linear(2, 4),      # 2 ingressi → 4 neuroni nascosti (pesi 2x4 + bias 4)
    nn.Tanh(),            # attivazione
    nn.Linear(4, 1),      # 4 → 1 uscita
    nn.Sigmoid(),         # uscita come probabilità
)
sum(p.numel() for p in rete.parameters())     # numero di parametri: 2·4+4 + 4·1+1 = 17
```

Per reti più articolate si definisce una classe che estende `nn.Module`:

```python
class Rete(nn.Module):
    def __init__(self):
        super().__init__()
        self.livello1 = nn.Linear(784, 128)
        self.livello2 = nn.Linear(128, 10)
    def forward(self, x):
        x = x.view(x.size(0), -1)             # appiattisce le immagini (N, 1, 28, 28) → (N, 784)
        x = torch.relu(self.livello1(x))
        return self.livello2(x)               # logits: punteggi grezzi, SENZA softmax
```

### Perdite

- `nn.MSELoss()`: regressione.
- `nn.BCELoss()`: binaria, con uscita già passata per la sigmoide (`nn.BCEWithLogitsLoss` accetta i logits
  ed è più stabile).
- `nn.CrossEntropyLoss()`: **multiclasse**. Riceve i **logits** (punteggi grezzi, forma `(N, classi)`) e
  le **etichette come interi** (forma `(N,)`, valori 0…classi−1). Applica da sé la softmax: **non**
  mettere una softmax alla fine della rete.

### Il ciclo di addestramento (da imparare a memoria)

```python
ottimizzatore = torch.optim.Adam(rete.parameters(), lr=0.001)
perdita_fn = nn.CrossEntropyLoss()

for epoca in range(n_epoche):
    for X_batch, y_batch in dati:
        ottimizzatore.zero_grad()              # 1. azzera i gradienti
        uscita = rete(X_batch)                 # 2. forward
        perdita = perdita_fn(uscita, y_batch)  # 3. perdita
        perdita.backward()                     # 4. backpropagation
        ottimizzatore.step()                   # 5. aggiorna i pesi
```

Cinque righe: `zero_grad`, forward, perdita, `backward`, `step`. **È tutto qui.**
Confrontale con il training loop del Modulo 3: stessa struttura.

### Dati a mini-batch

```python
from torch.utils.data import DataLoader, TensorDataset
dataset = TensorDataset(X_tensor, y_tensor)
dati = DataLoader(dataset, batch_size=64, shuffle=True)       # shuffle: ordine diverso a ogni epoca
```

Per i dataset di immagini `torchvision.datasets` fornisce `MNIST` pronto (Modulo 6).

### Valutare

```python
rete.eval()                          # modalità di valutazione (disattiva dropout, ecc.)
with torch.no_grad():                # niente gradienti
    uscita = rete(X_test)
    previsioni = uscita.argmax(dim=1)                # classe con il punteggio più alto
    accuratezza = (previsioni == y_test).float().mean().item()
rete.train()                         # tornare alla modalità di addestramento
```

### Salvare e caricare

```python
torch.save(rete.state_dict(), "modello.pt")             # salva i pesi (file ignorato da git)
rete.load_state_dict(torch.load("modello.pt"))          # ricarica (nella stessa architettura)
```

## 10. Errori comuni

| Sintomo | Causa probabile |
|---|---|
| La perdita non scende per niente | `zero_grad()` fuori posto; learning rate troppo piccolo; ottimizzatore non collegato ai parametri della rete |
| Perdita `nan` | learning rate troppo alto; input non normalizzati; `log(0)` |
| `RuntimeError: mat1 and mat2 shapes cannot be multiplied` | dimensioni di `nn.Linear` non coerenti con l'ingresso: controlla `.shape` |
| `CrossEntropyLoss` con errori sui tipi | le etichette devono essere `long` (interi): `y.long()` |
| Accuratezza peggiore di quanto previsto dopo l'addestramento | dimenticato `rete.eval()` o `torch.no_grad()`; ingressi non normalizzati come in training |
| Memoria che cresce | accumulare la perdita come tensore: usare `perdita.item()` |
| Softmax aggiunta prima di `CrossEntropyLoss` | doppia softmax: la rete impara male. Usare i logits |
| Training perfetto, test pessimo | overfitting: dropout, early stopping, più dati, rete più piccola |
| Risultati diversi a ogni esecuzione | seed non fissato: `torch.manual_seed(0)` |

**Procedura prudente per far funzionare una rete nuova:**
1. Far **sovra-adattare un piccolo gruppo di campioni** (es. 10): la perdita deve arrivare vicina a zero. Se
   non succede, c'è un errore nel codice, non nei dati.
2. Controllare forme e tipi di tutti i tensori.
3. Partire con `Adam`, `lr = 0.001`.
4. Disegnare la curva della perdita di training e della validazione per capire cosa succede.
