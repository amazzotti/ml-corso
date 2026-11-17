# Teoria 3 — NumPy, pandas e matplotlib

Gli strumenti per lavorare con i dati. Servono per il Modulo 2 e sono la base di tutto
il machine learning: i dati sono numeri organizzati in vettori, matrici e tabelle.

**Installazione** (con l'ambiente virtuale `.venv` attivo):

```powershell
pip install numpy pandas matplotlib
```

Convenzioni di import (si usano sempre così):

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Indice: [1. Vettori e matrici (matematica)](#1-vettori-e-matrici-matematica) ·
[2. NumPy: array](#2-numpy-array) · [3. NumPy: calcoli](#3-numpy-calcoli) ·
[4. NumPy: matrici](#4-numpy-matrici) · [5. Statistica essenziale](#5-statistica-essenziale) ·
[6. pandas](#6-pandas) · [7. Dati mancanti e pulizia](#7-dati-mancanti-e-pulizia) ·
[8. matplotlib](#8-matplotlib) · [9. Quale grafico scegliere](#9-quale-grafico-scegliere)

---

## 1. Vettori e matrici (matematica)

- **Vettore:** una lista ordinata di numeri. Es. `[3, 1, 4]`. Nel ML, un campione è spesso un
  vettore di caratteristiche: `[superficie, stanze, età_edificio]`.
- **Matrice:** una tabella di numeri con righe e colonne. Una matrice 3×2 ha 3 righe e 2 colonne.
  Un intero dataset è una matrice: una riga per campione, una colonna per caratteristica.
- **Operazioni elemento per elemento:** si applicano a numeri nella stessa posizione.
  `[1, 2, 3] + [10, 20, 30] = [11, 22, 33]`.
- **Prodotto riga per colonna** (prodotto matriciale): l'elemento in riga *i*, colonna *j*
  del risultato è la somma dei prodotti degli elementi della riga *i* della prima matrice
  per la colonna *j* della seconda.

```
A = [[1, 2],      B = [[0, 1],      A·B = [[1*0+2*1, 1*1+2*0],   = [[2, 1],
     [3, 4]]           [1, 0]]              [3*0+4*1, 3*1+4*0]]      [4, 3]]
```

Regola delle dimensioni: (a×b)·(b×c) → (a×c). Il numero di colonne della prima deve essere
uguale al numero di righe della seconda.

**Perché serve nel ML:** un livello di una rete neurale calcola esattamente un prodotto
matriciale tra i dati e una matrice di pesi.

## 2. NumPy: array

L'oggetto base è l'**array** (`np.ndarray`): una griglia di numeri **dello stesso tipo**,
molto più veloce di una lista Python.

```python
a = np.array([4, 8, 15, 16, 23, 42])
a.shape        # (6,)    forma: 6 elementi
a.ndim         # 1       numero di dimensioni
a.size         # 6       numero totale di elementi
a.dtype        # int64   tipo degli elementi
```

Creare array:

| Istruzione | Risultato |
|---|---|
| `np.array([1, 2, 3])` | `[1 2 3]` |
| `np.zeros(3)` | `[0. 0. 0.]` |
| `np.ones((2, 3))` | matrice 2×3 di uno |
| `np.arange(0, 10, 2)` | `[0 2 4 6 8]` (fine **escluso**, come `range`) |
| `np.linspace(0, 1, 5)` | `[0. 0.25 0.5 0.75 1.]` (5 punti, estremi **inclusi**) |
| `rng = np.random.default_rng(42)`<br>`rng.uniform(0, 10, 5)` | 5 numeri casuali tra 0 e 10 |
| `rng.normal(170, 10, 1000)` | 1000 valori da una gaussiana (media 170, dev. std. 10) |

Il numero `42` in `default_rng(42)` è il **seed**: con lo stesso seed si ottengono sempre gli
stessi numeri casuali (esperimenti ripetibili).

**Indicizzazione e slicing** (si parte da 0, come le liste):

```python
a[0]        # 4
a[-1]       # 42
a[1:4]      # [ 8 15 16]   (il 4 è escluso)
a[::2]      # [ 4 15 23]   (uno sì e uno no)
```

**Attenzione al tipo:** un array ha **un solo** `dtype`. `np.array([1, 2.5])` diventa
tutto `float`. Su Windows, con versioni vecchie di NumPy, gli interi di default possono
essere a 32 bit e andare in **overflow** con numeri molto grandi: in quel caso specifica
`dtype=np.int64`.

## 3. NumPy: calcoli

### Operazioni vettoriali

Le operazioni si applicano a **tutto l'array in una volta**, senza cicli `for`:

```python
a = np.arange(1, 6)          # [1 2 3 4 5]
a * 2                        # [ 2  4  6  8 10]
a ** 2                       # [ 1  4  9 16 25]
b = np.array([10, 20, 30, 40, 50])
a + b                        # [11 22 33 44 55]
a * b                        # elemento per elemento (NON prodotto matriciale)
np.sqrt(a)                   # radice di ciascun elemento
```

Si chiama **vettorializzazione**. È più leggibile e molto più veloce: NumPy esegue il ciclo
internamente in codice compilato (spesso 50–100 volte più veloce di un `for` Python).

### Broadcasting

Operare tra array di forme diverse: NumPy "allarga" quello più piccolo.

```python
M = np.array([[1, 2, 3],
              [4, 5, 6]])
M + 10                       # somma 10 a ogni elemento
M + np.array([100, 200, 300])    # somma il vettore a ciascuna riga
```

### Condizioni e maschere

```python
a = np.array([4, 8, 15, 16, 23, 42])
a > 10                       # [False False  True  True  True  True]
a[a > 10]                    # [15 16 23 42]   (filtro con maschera)
a[(a > 10) & (a < 30)]       # [15 16 23]      (& = e, | = o, ~ = non; servono le parentesi)
np.sum(a > 10)               # 4   (True vale 1: conta quanti soddisfano la condizione)
```

### Statistiche

```python
a.sum()      a.mean()      a.min()      a.max()
a.std()      np.median(a)  a.argmax()    # argmax: POSIZIONE del massimo
```

Per matrici, `axis` sceglie la direzione: `axis=0` lavora **lungo le righe, per colonna**
(un risultato per colonna); `axis=1` per riga.

```python
M.sum(axis=0)    # [5 7 9]   somma di ciascuna colonna
M.sum(axis=1)    # [ 6 15]   somma di ciascuna riga
```

## 4. NumPy: matrici

```python
M = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
M.shape          # (3, 4)   3 righe, 4 colonne
M[1, 2]          # 6        riga 1, colonna 2
M[0]             # [0 1 2 3]  prima riga
M[:, 0]          # [0 4 8]    prima colonna
M[1:, :2]        # righe dalla 1 in poi, prime due colonne
M.T              # trasposta: scambia righe e colonne, forma (4, 3)
M.reshape(2, 6)  # stessi numeri, nuova forma (il totale deve coincidere)
```

**Prodotto matriciale** con `@`:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
A @ B       # [[2 1] [4 3]]   prodotto riga per colonna
A * B       # [[0 2] [3 0]]   elemento per elemento (cosa DIVERSA!)
```

**Matrice per vettore** (il cuore di un livello di rete):

```python
W = np.array([[1, 0],
              [0, 1],
              [1, 1]])        # 3x2
x = np.array([2, 3])          # vettore di 2 elementi
W @ x                         # [2 3 5]   3 elementi
```

Errore comune: `ValueError: shapes (a,b) and (c,d) not aligned`. Significa che le dimensioni
non sono compatibili: controlla `.shape` di entrambi.

## 5. Statistica essenziale

Dato un insieme di valori *x₁ … xₙ*:

- **Media**: somma divisa per n. È il "centro di massa" dei dati.
- **Mediana**: il valore centrale una volta ordinati (se n è pari, media dei due centrali).
  È poco sensibile ai valori anomali (outlier): la media di `[1, 2, 3, 100]` è 26.5, la
  mediana 2.5.
- **Varianza**: media dei quadrati degli scarti dalla media, `mean((x - mean(x))**2)`.
  Misura quanto i dati sono sparpagliati.
- **Deviazione standard**: radice quadrata della varianza; ha la stessa unità dei dati.
  `a.std()` di NumPy calcola la deviazione standard "di popolazione" (divide per n).
- **Correlazione** (da −1 a +1): quanto due variabili variano insieme. +1: crescono insieme
  in modo perfettamente lineare; −1: una cresce e l'altra scende; 0: nessuna relazione
  lineare. `np.corrcoef(x, y)` o `df.corr()` in pandas. **Correlazione non è causalità.**

Esempio: `a = [4, 8, 15, 16, 23, 42]` → media 18, mediana 15.5, deviazione standard ≈ 12.3.

## 6. pandas

pandas lavora con **tabelle**. Due oggetti:

- **Series**: una colonna (valori + etichette degli indici).
- **DataFrame**: una tabella con righe e colonne con nome.

```python
df = pd.DataFrame({
    "nome": ["Anna", "Marco", "Luca"],
    "eta": [23, 25, 22],
    "voto": [28, 24, 30],
})
```

### Leggere e ispezionare

```python
df = pd.read_csv("studenti.csv")     # carica un file CSV
df.head()          # prime 5 righe (head(n) per n righe)
df.shape           # (righe, colonne)
df.info()          # colonne, tipi, valori non nulli
df.describe()      # statistiche per le colonne numeriche
df.columns         # nomi delle colonne
df["citta"].value_counts()    # quante righe per ciascun valore
```

Un file **CSV** è testo: una riga per record, valori separati da virgole, la prima riga è
l'intestazione. Si può scrivere con `df.to_csv("file.csv", index=False)`.

### Selezionare

```python
df["voto"]                  # una colonna (Series)
df[["nome", "voto"]]        # più colonne (DataFrame): doppie parentesi
df.loc[0]                   # riga con etichetta 0
df.iloc[0, 2]               # riga 0, colonna 2 (per posizione)
df.loc[df["voto"] >= 27]    # righe che soddisfano una condizione
```

### Filtrare

```python
df[df["voto"] >= 27]                          # condizione semplice
df[(df["citta"] == "Roma") & (df["voto"] >= 28)]   # & e |, parentesi obbligatorie
df[df["citta"].isin(["Roma", "Torino"])]
```

### Nuove colonne, ordinare

```python
df["promosso"] = df["voto"] >= 18          # nuova colonna booleana
df["voto_su_10"] = df["voto"] / 3
df.sort_values("voto", ascending=False)    # ordina per voto decrescente
df.sort_values("voto", ascending=False).head(3)    # i migliori 3
```

### Raggruppare

```python
df.groupby("citta")["voto"].mean()          # media del voto per città
df.groupby("citta")["voto"].agg(["mean", "count", "max"])
df.groupby("citta").size()                  # numero di righe per città
```

`groupby` divide in gruppi, calcola per ciascuno e ricompone: è la base di molte analisi.

### Altre operazioni utili

```python
df["voto"].mean()   df["voto"].max()   df["voto"].idxmax()   # idxmax: indice del massimo
df.corr(numeric_only=True)                  # matrice di correlazione
df.rename(columns={"eta": "età"})
df.drop(columns=["promosso"])
df["voto"].astype(float)                    # cambia tipo
```

## 7. Dati mancanti e pulizia

I dati reali sono sporchi: valori mancanti, duplicati, numeri scritti come testo.

```python
df.isna()                  # tabella di True/False
df.isna().sum()            # quanti mancanti per colonna
df.dropna()                # elimina le righe con almeno un mancante
df.dropna(subset=["voto"]) # solo se manca in quella colonna
df["voto"].fillna(df["voto"].mean())     # sostituisce con la media
df["citta"].fillna("sconosciuta")
df.duplicated()            # True per le righe duplicate (dalla seconda)
df.drop_duplicates()
pd.to_numeric(df["eta"], errors="coerce")   # testo -> numero; ciò che non si converte diventa NaN
```

`NaN` (*Not a Number*) è il valore mancante dei decimali.

Come scegliere tra eliminare e riempire:
- pochi mancanti in un dataset grande → eliminare è accettabile;
- tanti mancanti → riempire con media, **mediana** (più robusta) o un valore speciale;
- sempre **annotare** cosa è stato fatto: la pulizia influenza i risultati.

Ordine tipico: duplicati → tipi → mancanti → controllo finale con `info()` e `describe()`.

## 8. matplotlib

Un grafico è una **figura** con uno o più **assi** (`ax`). Il modo consigliato:

```python
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label="x al quadrato", color="tab:blue")
ax.set_title("Titolo")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
fig.savefig("grafico.png", dpi=150, bbox_inches="tight")
plt.show()
```

Tipi di grafico:

| Metodo | Uso | Esempio |
|---|---|---|
| `ax.plot(x, y)` | andamento (linea) | perdita durante l'addestramento |
| `ax.scatter(x, y)` | relazione tra due variabili | altezza contro peso |
| `ax.hist(valori, bins=20)` | distribuzione di una variabile | altezze di 1000 persone |
| `ax.bar(categorie, valori)` | confronto tra categorie | voto medio per città |
| `ax.axhline(y)` / `ax.axvline(x)` | linea di riferimento | la media |

Più grafici in una figura: `fig, assi = plt.subplots(1, 3, figsize=(15, 4))`, poi `assi[0]`,
`assi[1]`, `assi[2]`.

Scatter colorato per classe: `ax.scatter(x, y, c=classi)` (un numero per punto).

`plt.show()` apre una finestra; chiudila per far proseguire il programma. Per i programmi che
generano molti grafici conviene salvarli con `savefig` (cartella `grafici/`, ignorata da git).

## 9. Quale grafico scegliere

- **Una variabile numerica, voglio vedere come si distribuisce** → istogramma.
- **Due variabili numeriche, voglio vedere se sono collegate** → scatter.
- **Un valore che cambia nel tempo o nelle iterazioni** → linea.
- **Un valore per ciascuna categoria** → barre.
- Sempre: **titolo, etichette degli assi con unità, legenda se ci sono più serie**. Un grafico
  senza etichette non comunica niente.
- Non usare grafici a torta per più di 3–4 categorie, e non troncare l'asse delle barre
  (falsa l'impressione delle proporzioni).
