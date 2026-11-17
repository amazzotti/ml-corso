# Teoria 5 — Machine learning classico con scikit-learn

Classificazione, valutazione corretta dei modelli, overfitting, metriche e preparazione dei dati.
Serve per gli esercizi `modulo4/01` … `modulo4/08`. Prerequisiti: `03_numpy_pandas.md` e
`04_regressione_gradient_descent.md`.

**Installazione:** `pip install scikit-learn`

Indice: [1. Classificazione](#1-classificazione) · [2. Train, test e validazione](#2-train-test-e-validazione) ·
[3. L'interfaccia di scikit-learn](#3-linterfaccia-di-scikit-learn) · [4. Regressione logistica](#4-regressione-logistica) ·
[5. Alberi decisionali](#5-alberi-decisionali) · [6. Overfitting e underfitting](#6-overfitting-e-underfitting) ·
[7. Metriche di valutazione](#7-metriche-di-valutazione) · [8. Preparare i dati](#8-preparare-i-dati) ·
[9. Cross-validation](#9-cross-validation) · [10. Scegliere un modello](#10-scegliere-un-modello) ·
[11. Errori comuni](#11-errori-comuni)

---

## 1. Classificazione

Nella **classificazione** l'etichetta è una **categoria** (classe): cifra 0–9, specie di un fiore,
"sopravvissuto / non sopravvissuto". Il modello riceve le feature e restituisce una classe
(o, meglio, una **probabilità per ogni classe**).

- **Binaria:** due classi (sì/no, 0/1).
- **Multiclasse:** più di due classi (le tre specie di Iris, le dieci cifre).

Dataset usato negli esercizi: **Iris** — 150 fiori, 4 feature (lunghezza e larghezza di sepali e
petali, in cm), 3 specie (0 = setosa, 1 = versicolor, 2 = virginica), 50 campioni per specie.
Si carica senza scaricare nulla: `from sklearn.datasets import load_iris`.

## 2. Train, test e validazione

**Il punto fondamentale del machine learning:** a noi non interessa che il modello sia bravo sui
dati che ha già visto, ma che **funzioni su dati nuovi** (*generalizzazione*).

Un modello abbastanza flessibile può **imparare a memoria** i dati di addestramento (accuratezza 100%)
e comportarsi male su dati nuovi. Per accorgersene bisogna **misurare su dati che il modello non ha
mai visto**.

Quindi si divide il dataset:

- **Training set** (es. 70–80%): serve per **addestrare** (calcolare i parametri).
- **Test set** (es. 20–30%): serve **solo alla fine** per stimare le prestazioni reali. Non si usa mai
  per prendere decisioni sul modello.
- **Validation set** (opzionale, oppure ottenuto con la cross-validation): serve per **scegliere**
  iperparametri e confrontare modelli, lasciando il test intatto.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
```

- `test_size=0.3`: il 30% va nel test (su 150 campioni: 105 per l'addestramento, 45 per il test).
- `random_state=42`: seed per rendere la divisione ripetibile.
- `stratify=y`: mantiene le **stesse proporzioni di classi** in train e test (con Iris: 15 per classe
  nel test). Importante con classi sbilanciate o dataset piccoli.

**Data leakage (perdita di informazioni):** errore gravissimo e sottile. Succede quando informazioni
del test set "entrano" nell'addestramento: per esempio calcolare media e deviazione standard su
**tutto** il dataset prima di dividerlo, oppure scegliere gli iperparametri guardando il test.
Regola: **ogni trasformazione si "impara" (fit) solo sul training set** e poi si applica al test.

Il risultato dipende dalla divisione, specie con pochi dati: due divisioni diverse possono dare
accuratezze diverse (es. 93% e 100% su Iris). Per questo esiste la cross-validation (sezione 9).

## 3. L'interfaccia di scikit-learn

Tutti i modelli di scikit-learn funzionano allo stesso modo:

```python
from sklearn.linear_model import LogisticRegression

modello = LogisticRegression(max_iter=200)    # 1. crea il modello (con gli iperparametri)
modello.fit(X_train, y_train)                 # 2. ADDESTRA sui dati di training
y_pred = modello.predict(X_test)              # 3. prevedi le classi
prob = modello.predict_proba(X_test)          # 3b. probabilità per ogni classe
acc = modello.score(X_test, y_test)           # 4. accuratezza sul test
```

- `fit` è l'addestramento (per la regressione logistica usa un algoritmo di ottimizzazione simile
  al gradient descent).
- `X` ha forma `(n_campioni, n_feature)`, `y` forma `(n_campioni,)`.
- Cambiare modello vuol dire cambiare **una riga**: `DecisionTreeClassifier(...)`,
  `KNeighborsClassifier(...)`, ecc.

**Pipeline:** concatena preparazione dei dati e modello in un unico oggetto, così le trasformazioni
vengono imparate sul solo training ed evitano il leakage (sezione 8).

## 4. Regressione logistica

Nonostante il nome, serve per la **classificazione**. Idea: parte come la regressione lineare e
trasforma il risultato in una **probabilità**.

```
z = w₁·x₁ + w₂·x₂ + … + b                 (punteggio lineare, qualsiasi numero reale)
p = σ(z) = 1 / (1 + e^(−z))               (sigmoide: schiaccia z nell'intervallo 0…1)
```

- Se z è molto positivo, p ≈ 1; se è molto negativo, p ≈ 0; se z = 0, p = 0.5.
- **p** è la probabilità stimata della classe 1. Regola di decisione: classe 1 se p ≥ 0.5.
- Per più di due classi si usa la **softmax**: un punteggio per classe, trasformati in probabilità
  che sommano 1.

**Perdita:** non l'errore quadratico, ma la **cross-entropy** (*log loss*):

```
L = −(1/N) · Σ [ yᵢ·log(pᵢ) + (1 − yᵢ)·log(1 − pᵢ) ]
```

Intuizione: se il campione è di classe 1 e il modello dà p = 0.99, la perdita è bassa
(−log 0.99 ≈ 0.01); se dà p = 0.01 è altissima (−log 0.01 ≈ 4.6). La cross-entropy **punisce
fortemente le previsioni sicure e sbagliate**.

L'addestramento è lo **stesso schema del Modulo 3**: perdita → gradiente → passi di discesa.
Questa stessa perdita e la sigmoide/softmax ritorneranno nelle reti neurali.

Pregi: semplice, veloce, interpretabile (i pesi dicono quali feature contano e in che verso).
Limiti: il confine tra le classi è **lineare** (una retta/un piano).

## 5. Alberi decisionali

Un **albero** è una sequenza di domande sì/no sulle feature, come un diagramma di flusso:

```
petal width <= 0.8 ?
├── sì → setosa
└── no → petal width <= 1.75 ?
         ├── sì → (altre domande) → versicolor
         └── no → virginica
```

**Come impara:** a ogni nodo sceglie la domanda (feature + soglia) che separa meglio le classi.
La "purezza" di un gruppo si misura con l'**impurità di Gini**:

```
Gini = 1 − Σ pₖ²      (pₖ = frazione di campioni della classe k nel gruppo)
```

- Gruppo puro (tutti della stessa classe): Gini = 1 − 1² = **0**.
- Gruppo 50/50 fra due classi: Gini = 1 − (0.5² + 0.5²) = **0.5** (massima impurità).
- Esempio: 8 campioni di classe A e 2 di classe B → p = 0.8 e 0.2 → Gini = 1 − (0.64 + 0.04) = 0.32.

Per ogni domanda candidata si calcola la Gini media dei due gruppi risultanti (pesata per la
numerosità); si sceglie la domanda che la riduce di più. Si ripete in ciascun gruppo.

**Iperparametri che controllano la complessità:**
- `max_depth`: profondità massima (numero di domande in fila). Albero profondo = complesso.
- `min_samples_leaf`: numero minimo di campioni in una foglia.

**Pregi:** si capiscono e si disegnano; non richiedono standardizzazione; gestiscono relazioni non
lineari. **Limiti:** senza limiti di profondità **si adattano perfettamente ai dati di addestramento**
(accuratezza 100%) e fanno **overfitting**; piccoli cambiamenti nei dati danno alberi molto diversi.

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
albero = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_train, y_train)
albero.feature_importances_            # quanto ogni feature contribuisce
export_text(albero, feature_names=list(X.columns))      # regole in testo
plot_tree(albero, feature_names=list(X.columns), filled=True)   # disegno
```

## 6. Overfitting e underfitting

- **Underfitting:** il modello è **troppo semplice** per cogliere la struttura dei dati. Va male
  sia sul training che sul test. (Esempio: una retta per dati curvi; un albero profondo 1.)
- **Overfitting:** il modello è **troppo complesso** e impara anche il rumore. Va benissimo sul
  training e peggio sul test. (Esempio: un albero senza limite di profondità.)
- **Giusto equilibrio:** buon risultato su entrambi, con poca differenza.

Il segnale diagnostico è il **divario tra accuratezza di training e di test**:

| Training | Test | Diagnosi |
|---|---|---|
| bassa | bassa | underfitting |
| alta | molto più bassa | **overfitting** |
| alta | alta (simile) | buon modello |

**Curva di complessità:** al crescere della complessità (profondità dell'albero) l'accuratezza di
**training sale sempre** fino al 100%, mentre quella di **test sale, raggiunge un massimo e poi
scende**. Si sceglie la complessità vicina al massimo del test (o della validazione).

**Rimedi all'overfitting:** più dati; modello più semplice (meno profondità, meno parametri);
**regolarizzazione** (penalizzare i pesi grandi); **early stopping** (fermare l'addestramento
quando la validazione peggiora); **dropout** (nelle reti neurali); **data augmentation**.

**Rimedi all'underfitting:** modello più complesso, più feature, addestramento più lungo.

## 7. Metriche di valutazione

L'**accuratezza** è la frazione di previsioni corrette: `corrette / totali`. È intuitiva ma
**può ingannare**.

**Esempio.** Un dataset ha 95% di campioni "sano" e 5% "malato". Un "modello" che risponde
sempre "sano" ha **accuratezza 95%** ma **non trova nessun malato**: è inutile. Con classi
sbilanciate serve altro.

**Matrice di confusione** (caso binario, classe "positiva" = quella che ci interessa trovare):

|  | Previsto positivo | Previsto negativo |
|---|---|---|
| **Realmente positivo** | VP (vero positivo) | FN (falso negativo) |
| **Realmente negativo** | FP (falso positivo) | VN (vero negativo) |

```
accuratezza = (VP + VN) / totale
precisione  = VP / (VP + FP)     "quando dico positivo, quante volte ho ragione?"
recall      = VP / (VP + FN)     "dei veri positivi, quanti ne trovo?"   (sensibilità)
F1          = 2 · precisione · recall / (precisione + recall)     (media armonica)
```

Esempio: 100 malati reali; il modello ne trova 60 (VP = 60, FN = 40) e segnala 20 sani come
malati (FP = 20). Precisione = 60/80 = 0.75; recall = 60/100 = 0.60;
F1 = 2·0.75·0.60 / 1.35 = 0.667.

**Quale scegliere:** se un falso negativo è grave (malattia non diagnosticata) conta il **recall**;
se un falso positivo è grave (accusare un innocente, bloccare un cliente onesto) conta la
**precisione**. Spesso c'è un compromesso e si cambia la **soglia** di decisione (non per forza 0.5).

```python
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             precision_score, recall_score, f1_score, classification_report)
confusion_matrix(y_test, y_pred)          # righe = classe reale, colonne = classe prevista
precision_score(y_test, y_pred, zero_division=0)
classification_report(y_test, y_pred)     # tabella riassuntiva
```

In `confusion_matrix` di scikit-learn per il caso binario l'ordine è `[[VN, FP], [FN, VP]]`.

**Strumenti per classi sbilanciate:** `class_weight="balanced"` (pesa di più gli errori sulla classe
rara, aumenta il recall a scapito della precisione), ricampionamento, scelta della soglia, e **sempre**
confrontare con un modello "stupido" di riferimento (`DummyClassifier`): se il tuo modello non lo
batte, non ha imparato niente.

Per la **regressione** si usano altre metriche: MSE/RMSE, MAE, R² (vedi teoria 04).

## 8. Preparare i dati

I dati reali non vanno dati ai modelli così come sono.

**Valori mancanti.** La maggior parte dei modelli non accetta `NaN`. Si **imputano**:
`SimpleImputer(strategy="median")` per i numeri (la mediana è robusta), `"most_frequent"` per le
categorie.

**Variabili categoriche** (testo come "maschio/femmina", "C/Q/S"): i modelli vogliono numeri.
**One-hot encoding:** una colonna 0/1 per ogni categoria. Mai numerarle 0,1,2 se non c'è un ordine
naturale (il modello penserebbe che 2 sia "più di" 1).
`OneHotEncoder(handle_unknown="ignore")`.

**Scalatura (standardizzazione).** `StandardScaler`: `(x − media) / dev. std.` Necessaria per modelli
basati su distanze o su gradienti (regressione logistica, reti neurali, k-NN); non serve per gli
alberi. Ricorda dal Modulo 3: feature con scale molto diverse rallentano o rompono l'addestramento.

**Pipeline e ColumnTransformer:** applicano trasformazioni diverse a colonne diverse e le
concatenano al modello.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

num = ["age", "fare"]
cat = ["sex", "embarked"]
pre = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]), num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat),
])
modello = Pipeline([("pre", pre), ("clf", LogisticRegression(max_iter=1000))])
modello.fit(X_train, y_train)       # imputazione, scalatura e modello imparati SOLO sul training
modello.score(X_test, y_test)
```

Il grande vantaggio: nessun **leakage**, perché il `fit` della pipeline impara tutto dal solo training.

## 9. Cross-validation

Una sola divisione train/test può essere fortunata o sfortunata. La **k-fold cross-validation**
divide i dati in *k* parti (fold); per ciascuna volta, una parte fa da test e le altre *k−1* da
training; si ottengono *k* punteggi.

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
punteggi = cross_val_score(modello, X, y, cv=cv)
print(punteggi.mean(), punteggi.std())      # media ± deviazione standard
```

- La **media** stima la prestazione; la **deviazione standard** dice quanto è affidabile la stima.
- `shuffle=True` è importante se i dati sono **ordinati** (es. il dataset Titanic è ordinato per
  classe del passeggero: senza mescolare i fold sono molto diversi tra loro).
- Con una pipeline la cross-validation rifà l'intero `fit` (imputazione compresa) in ogni fold:
  corretto e senza leakage.

## 10. Scegliere un modello

Procedura corretta:
1. Tieni da parte un **test set** e non toccarlo.
2. Con cross-validation sul solo training confronta modelli e iperparametri (es. diverse profondità).
3. Scegli il migliore.
4. **Una sola volta**, valutalo sul test set: quello è il numero da riportare.

Confrontare i modelli sempre contro un **riferimento semplice** (Dummy) e contro un modello
semplice come la regressione logistica. Modelli più complessi non sono automaticamente migliori:
se la differenza è minore della deviazione standard della cross-validation, **non c'è differenza
significativa**; a parità di prestazioni si preferisce il modello più semplice.

## 11. Errori comuni

| Errore | Conseguenza | Come evitarlo |
|---|---|---|
| Valutare sul training set | prestazioni gonfiate | sempre un test set |
| Scalare/imputare su tutto il dataset prima dello split | leakage, stime ottimistiche | Pipeline |
| Scegliere iperparametri guardando il test | il test non è più "mai visto" | validazione / cross-validation |
| Guardare solo l'accuratezza con classi sbilanciate | modello inutile ma "al 95%" | precisione, recall, F1, Dummy |
| Una sola divisione train/test con pochi dati | risultato dipende dalla fortuna | cross-validation |
| Numerare le categorie 0,1,2 | ordine inesistente | one-hot |
| Non fissare `random_state` | risultati non ripetibili | seed fissi negli esperimenti |
| Confrontare modelli senza confronto con riferimento | non si sa se hanno imparato | `DummyClassifier` |
| Interpretare correlazione come causalità | conclusioni sbagliate | cautela, esperimenti |
