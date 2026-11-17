"""Esercizio 6 (Modulo 4) - Metriche: perche' l'accuratezza puo' ingannare.

Teoria: teoria/05_ml_classico.md, sezione 7.

OBIETTIVO
Scoprire che su un dataset sbilanciato un modello inutile puo' avere il 95% di
accuratezza, e imparare a leggere matrice di confusione, precisione, recall, F1.

PARTE A - A MANO, SENZA LIBRERIE
Un modello di diagnosi su 200 pazienti: 20 realmente malati (classe positiva).
Il modello ne segnala 18 come malati; di questi 15 lo sono davvero.
1. Costruisci la matrice (positivo = malato):
       VP (veri positivi)  = 15
       FP (falsi positivi) = 18 - 15 = 3
       FN (falsi negativi) = 20 - 15 = 5
       VN (veri negativi)  = 200 - 15 - 3 - 5 = 177
2. Calcola con Python:
       accuratezza = (VP + VN) / 200         = 0.960
       precisione  = VP / (VP + FP)          = 15/18 = 0.833
       recall      = VP / (VP + FN)          = 15/20 = 0.750
       F1          = 2*p*r / (p + r)         = 0.789
3. Scrivi in un commento a parole: la precisione risponde a "quando il modello dice
   malato, quante volte ha ragione?"; il recall a "dei veri malati, quanti ne trova?".

PARTE B - DATASET SBILANCIATO
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=2000, n_features=10, n_informative=4,
                               weights=[0.95, 0.05], flip_y=0.01, random_state=0)
Solo circa il 5% dei campioni e' positivo (108 su 2000).
Dividi con  test_size=0.3, random_state=0, stratify=y  (nel test: 32 positivi su 600).
1. Modello "stupido":
       from sklearn.dummy import DummyClassifier
       dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
   Calcola accuratezza, precisione, recall (usa zero_division=0 nella precisione):
       accuratezza 0.947   precisione 0.000   recall 0.000
   Predice SEMPRE "negativo": ha il 94,7% di accuratezza senza trovare nessun positivo!
2. Regressione logistica (max_iter=1000):
       accuratezza 0.947   precisione 0.000   recall 0.000
   Matrice di confusione: [[568, 0], [32, 0]]. Pur essendo un vero modello, qui impara a dire
   sempre "negativo" perche' e' il modo piu' semplice di ridurre l'errore medio.
   Ha esattamente le stesse prestazioni del modello stupido.
3. Albero di profondita' 5 (random_state=0):
       accuratezza 0.948   precisione 0.556   recall 0.156   F1 0.244
   Trova qualche positivo (15%) con una precisione del 56%.
4. Regressione logistica con  class_weight="balanced"  (pesa di piu' gli errori sulla classe rara):
       accuratezza 0.563   precisione 0.074   recall 0.625   F1 0.132
   L'accuratezza CROLLA (56%), ma ora trova il 62,5% dei positivi (a costo di tanti falsi positivi).
5. Compila una tabella (nel codice o come commento) con le quattro righe e le quattro metriche.
   Quale modello e' "migliore"? Dipende dal costo degli errori: se mancare un
   positivo e' grave, preferisci il recall; se un falso allarme costa molto, la precisione.

PARTE C - IL REPORT COMPLETO
    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred, zero_division=0))
Leggi la tabella: per ogni classe precisione, recall, F1, e "support" (quanti campioni).

CONCETTI NUOVI
- Matrice di confusione: VP, FP, FN, VN. In scikit-learn (binario):  [[VN, FP], [FN, VP]].
- Accuratezza, precisione, recall, F1 con formule ed esempi.
- Classi sbilanciate e modello di riferimento (Dummy).
- class_weight="balanced" e il compromesso precisione/recall.
- zero_division=0: evita avvisi quando il modello non predice mai la classe positiva.

COME VERIFICARE DA SOLO
    assert abs(accuratezza_A - 0.96) < 1e-9
    assert abs(precisione_A - 15 / 18) < 1e-9 and abs(recall_A - 0.75) < 1e-9
    assert abs(f1_A - 0.7895) < 1e-3
    assert abs(dummy.score(X_test, y_test) - 0.947) < 0.002
    assert recall_balanced > recall_logreg      # il modello bilanciato trova piu' positivi

ERRORI TIPICI
- Valutare un modello di classi sbilanciate solo con l'accuratezza.
- Non confrontare con un modello di riferimento.
- Leggere la matrice di confusione di scikit-learn con VP in alto a sinistra:
  nel binario lo e' in BASSO a destra.
- Dimenticare stratify=y: nel test potrebbero finire pochissimi positivi.

BONUS (facoltativo)
- Cambia la soglia di decisione: usa predict_proba e classifica positivo se p > 0.1
  (invece di 0.5). Osserva come recall e precisione si muovono in direzioni opposte.
- Disegna la curva precisione-recall o la curva ROC (sklearn.metrics.RocCurveDisplay)
  e calcola l'AUC.
- Calcola le metriche a mano da confusion_matrix(...).ravel() e verifica che
  coincidano con quelle di scikit-learn.

Scrivi il tuo codice qui sotto.
"""

