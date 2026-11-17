"""Esercizio 4 (Modulo 4) - Albero decisionale.

Teoria: teoria/05_ml_classico.md, sezione 5.

OBIETTIVO
Addestrare un albero decisionale, leggerne le regole, e vedere come la
profondita' ne controlla la complessita'.

PASSI
Usa la divisione dell'esercizio 2 (test_size=0.3, random_state=42, stratify=y).
1. Addestra alberi di profondita' diversa e stampa training e test:
       for d in [1, 2, 3, None]:
           albero = DecisionTreeClassifier(max_depth=d, random_state=0)
           albero.fit(X_train, y_train)
   Risultati attesi (accuratezza train / test):
       profondita' 1      0.667 / 0.667
       profondita' 2      0.971 / 0.889
       profondita' 3      0.981 / 0.933
       senza limite       1.000 / 0.978
   (None = nessun limite.)
   Leggi i numeri:
   - profondita' 1: UNDERFITTING (un'unica domanda separa solo una classe;
     le altre due restano mescolate: 2 classi su 3 -> 0.667).
   - senza limite: training perfetto (100%) ma gia' un piccolo divario col test.
2. Prendi l'albero di profondita' 3 e leggi le sue regole in testo:
       from sklearn.tree import export_text
       print(export_text(albero, feature_names=list(X.columns)))
   Con questa divisione l'output atteso e':
       |--- petal width (cm) <= 0.70
       |   |--- class: 0
       |--- petal width (cm) >  0.70
       |   |--- petal width (cm) <= 1.55
       |   |   |--- petal length (cm) <= 4.95
       |   |   |   |--- class: 1
       |   |   |--- petal length (cm) >  4.95
       |   |   |   |--- class: 2
       |   |--- petal width (cm) >  1.55
       |   |   |--- petal length (cm) <= 4.85
       |   |   |   |--- class: 1
       |   |   |--- petal length (cm) >  4.85
       |   |   |   |--- class: 2
   La prima domanda isola la setosa con una soglia sulla larghezza del petalo
   (le soglie esatte possono variare un po' con la versione di scikit-learn).
   Leggi l'albero come un diagramma di flusso: ogni fiore percorre un cammino
   fino a una foglia, che da' la classe.
3. Disegna l'albero (salva in modulo4/grafici/04_albero.png):
       from sklearn.tree import plot_tree
       fig, ax = plt.subplots(figsize=(14, 8))
       plot_tree(albero, feature_names=list(X.columns),
                 class_names=list(iris.target_names), filled=True, ax=ax)
   In ogni nodo trovi: la domanda, il valore "gini" (impurita'), "samples"
   (campioni arrivati li') e la classe prevalente. Le foglie hanno gini 0
   (o quasi): gruppi puri.
4. Importanza delle feature:
       albero.feature_importances_
   Attese: petal width 0.959, petal length 0.041, le due dei sepali 0.0.
   Solo le feature dei petali contano, in particolare la larghezza: conferma
   quello che hai visto nell'esercizio 1.
5. Verifica a mano un calcolo di Gini: un gruppo con 8 campioni della classe A e 2
   della classe B ha Gini = 1 - (0.8^2 + 0.2^2) = 0.32. Scrivi la funzione
   gini(conteggi) e provala: gini([8, 2]) -> 0.32, gini([10, 0]) -> 0,
   gini([5, 5]) -> 0.5.

CONCETTI NUOVI
- Albero = sequenza di domande sulle feature (if/else appresi dai dati).
- Impurita' di Gini: 0 = gruppo puro, 0.5 = massimo disordine (2 classi).
- max_depth: iperparametro di complessita'.
- Underfitting (troppo semplice) e overfitting (troppo complesso).
- feature_importances_: quanto ogni feature contribuisce.

COME VERIFICARE DA SOLO
    assert abs(albero_3.score(X_test, y_test) - 0.933) < 0.002
    assert albero_senza_limite.score(X_train, y_train) == 1.0
    assert abs(gini([8, 2]) - 0.32) < 1e-9 and gini([10, 0]) == 0
    assert abs(gini([5, 5]) - 0.5) < 1e-9
(I valori possono variare di poco tra versioni diverse di scikit-learn.)

ERRORI TIPICI
- Dimenticare random_state: alberi leggermente diversi a ogni esecuzione.
- Confondere max_depth=None (nessun limite) con 0.
- Pensare che un albero con 100% di training sia "il migliore": e' un campanello
  d'allarme, non un traguardo.
- plot_tree senza figsize abbastanza grande: testo illeggibile.

BONUS (facoltativo)
- Prova min_samples_leaf=5 al posto di max_depth e confronta.
- Calcola a mano la prima divisione: per la soglia "petal length <= 2.45" conta
  quanti campioni di ciascuna classe vanno a sinistra e a destra e calcola la
  Gini media pesata dei due gruppi.
- Dai all'albero un'altra divisione (random_state=1): le prime regole sono le stesse?
  La stabilita' e' un punto debole degli alberi.

Scrivi il tuo codice qui sotto.
"""

