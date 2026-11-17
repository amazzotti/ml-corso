"""Esercizio 8 (Modulo 4) - Confronto tra modelli con la cross-validation.

Teoria: teoria/05_ml_classico.md, sezioni 9 e 10.

OBIETTIVO
Confrontare piu' modelli in modo affidabile con la cross-validation, e scegliere
usando media e deviazione standard dei punteggi, non un singolo numero.

PARTE A - WARM-UP SU IRIS
    from sklearn.model_selection import cross_val_score
    punteggi = cross_val_score(modello, X, y, cv=5)
1. Per ciascuno di questi modelli stampa i 5 punteggi, la media e la deviazione standard:
       LogisticRegression(max_iter=200)
       DecisionTreeClassifier(max_depth=3, random_state=0)
       KNeighborsClassifier(n_neighbors=5)
   Attesi (media +- dev. std.):
       logistica  0.973 +- 0.025
       albero     0.960 +- 0.025
       k-NN       0.973 +- 0.025
   Le differenze (0.013) sono MINORI della deviazione standard (0.025): su Iris non
   c'e' differenza significativa. Scrivilo in un commento.

PARTE B - TITANIC (usa la preparazione dell'esercizio 7)
Costruisci le Pipeline (preprocessing + modello) per 5 modelli:
       DummyClassifier(strategy="most_frequent")
       LogisticRegression(max_iter=1000)
       DecisionTreeClassifier(max_depth=3, random_state=0)
       DecisionTreeClassifier(random_state=0)                     (senza limite)
       RandomForestClassifier(n_estimators=200, random_state=0)
Usa una cross-validation con rimescolamento (IMPORTANTE: il Titanic e' ordinato per
classe del biglietto, senza shuffle i fold sono molto diversi):
       from sklearn.model_selection import StratifiedKFold
       cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
       cross_val_score(pipeline, X, y, cv=cv)
Risultati attesi (media +- dev. std.):
       Dummy              0.618 +- 0.001
       Regressione log.   0.778 +- 0.018
       Albero profondita' 3   0.808 +- 0.011
       Albero senza limite    0.763 +- 0.019
       Random forest      0.794 +- 0.019
Osservazioni da scrivere in un commento:
   - tutti battono nettamente il Dummy (0.618): i modelli hanno imparato qualcosa;
   - l'albero semplice (profondita' 3) e' il MIGLIORE; quello senza limite e' tra i
     peggiori (overfitting, training 0.97 contro 0.76 in cross-validation);
   - la random forest (centinaia di alberi insieme) non e' migliore dell'albero semplice
     qui: modelli complessi non vincono per forza;
   - la differenza tra regressione logistica (0.778) e forest (0.794) e' dello stesso ordine
     della deviazione standard (0.018): non e' significativa.

PARTE C - LA VALUTAZIONE FINALE (la regola d'oro)
1. Tieni da parte un test set (25%, stratificato) PRIMA di tutto.
2. Confronta i modelli con la cross-validation SOLO sul training.
3. Scegli il migliore (albero a profondita' 3).
4. Valutalo UNA volta sul test set:   test 0.838 (con lo split dell'esercizio 7).
Scrivi in un commento perche' il test set non va usato per scegliere il modello.

PARTE D - TABELLA RIASSUNTIVA
Costruisci un DataFrame pandas con colonne: modello, media, std, e stampalo ordinato
per media decrescente. Salvalo come CSV in modulo4/risultati_confronto.csv
(file generato, non indispensabile pubblicarlo).

CONCETTI NUOVI
- k-fold cross-validation e StratifiedKFold con shuffle.
- Media e deviazione standard dei punteggi: quanto fidarsi della stima.
- Differenza significativa o no: confrontare la differenza di media con la dev. std.
- Scelta del modello senza toccare il test.
- Confronto con il Dummy e preferenza per il modello piu' semplice a parita' di prestazioni.

COME VERIFICARE DA SOLO
    assert abs(media_iris["logistica"] - 0.973) < 0.005
    assert abs(media_titanic["dummy"] - 0.618) < 0.005
    assert media_titanic["albero_3"] > media_titanic["albero_pieno"]
    assert all(m > media_titanic["dummy"] for k, m in media_titanic.items() if k != "dummy")

ERRORI TIPICI
- cross_val_score con cv=5 su dati ordinati (Titanic): stime molto variabili e
  fuorvianti (deviazioni standard intorno a 0.10 e medie diverse).
- Mettere il preprocessing FUORI dalla pipeline e fare il fit su tutto il dataset: leakage.
- Scegliere il modello guardando il test e riportare quel numero come "prestazione":
  e' ottimistico.
- Dimenticare random_state e non riuscire a ripetere il confronto.

BONUS (facoltativo)
- Aggiungi un grafico a barre con le medie e barre d'errore (yerr=std).
- Cerca la migliore profondita' dell'albero (1-10) con cross-validation:
  from sklearn.model_selection import GridSearchCV. Quale scegli?
- Calcola anche la precisione e il recall in cross-validation con cross_validate e
  scoring=["accuracy", "precision", "recall"].
- Chiudi il modulo scrivendo "modulo4/riassunto.md": 8-10 righe su train/test,
  overfitting, metriche e cross-validation, con parole tue.

Scrivi il tuo codice qui sotto.
"""

