"""Esercizio 2 (Modulo 4) - Training set e test set.

Teoria: teoria/05_ml_classico.md, sezione 2.

OBIETTIVO
Capire perche' si dividono i dati in due parti, dividerli correttamente e
vedere con i tuoi occhi che valutare sul training set inganna.

PARTE A - LA DIVISIONE
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
(X e y: dataset Iris, come nell'esercizio 1.)
1. Stampa le dimensioni:
       len(X_train) = 105    len(X_test) = 45
2. Quanti fiori per classe nel test? Con stratify=y: 15 / 15 / 15.
   Ripeti la divisione SENZA stratify=y e guarda le proporzioni di classe nel
   test (cambiano: con stratify restano uguali al dataset originale).
3. Cambia random_state (0, 1, 2, ...) e osserva che la divisione cambia.
   Rimetti 42: il random_state rende l'esperimento RIPETIBILE.

PARTE B - PERCHE' SERVE IL TEST
Usa un modello molto flessibile, un albero senza limiti di profondita':
    from sklearn.tree import DecisionTreeClassifier
    albero = DecisionTreeClassifier(random_state=0)
    albero.fit(X_train, y_train)
1. Accuratezza sul training:  albero.score(X_train, y_train)  ->  1.000
2. Accuratezza sul test:      albero.score(X_test, y_test)    ->  0.978
   Sul training e' perfetta perche' l'albero ha imparato "a memoria" i 105
   fiori. Il test (mai visto) dice la verita': 0.978. Il divario tra i due
   numeri e' il segnale dell'overfitting (qui piccolo, perche' Iris e' facile).
3. Se avessi misurato solo sul training avresti detto "100%": una stima troppo
   ottimistica. Scrivilo in un commento con parole tue.

PARTE C - LA DIVISIONE DIPENDE DALLA FORTUNA
Ripeti la parte B per 20 valori di random_state da 0 a 19 e raccogli le
accuratezze di test in una lista.
1. Stampa minimo, massimo, media e deviazione standard.
   Con la divisione stratificata (test_size=0.3, stratify=y) i valori attesi sono:
   minimo 0.889, massimo 1.000, media circa 0.95, deviazione standard circa 0.03.
   (45 campioni di test: ogni errore in piu' costa 2,2 punti percentuali.)
2. Conclusione da scrivere in un commento: con pochi dati UNA sola divisione
   da' una stima poco affidabile. Nell'esercizio 8 vedrai la cross-validation,
   che risolve il problema.

CONCETTI NUOVI
- Training set: per imparare. Test set: per valutare, mai usato per imparare.
- test_size, random_state (ripetibilita'), stratify (stesse proporzioni di classi).
- Overfitting: accuratezza alta sul training, piu' bassa sul test.
- Una stima da un solo test set e' soggetta a fortuna.

COME VERIFICARE DA SOLO
    assert len(X_train) == 105 and len(X_test) == 45
    assert y_test.value_counts().tolist() == [15, 15, 15]
    assert albero.score(X_train, y_train) == 1.0
    assert abs(albero.score(X_test, y_test) - 0.978) < 0.001
    assert albero.score(X_train, y_train) >= albero.score(X_test, y_test)

ERRORI TIPICI
- Addestrare (fit) su X intero e poi valutare sul test: il modello ha gia' visto
  quei dati (DATA LEAKAGE).
- Dimenticare che train_test_split restituisce QUATTRO oggetti, in un ordine preciso:
  X_train, X_test, y_train, y_test.
- Scambiare X_test e y_test nell'assegnazione.
- Non fissare random_state e non riuscire a ripetere un risultato.

BONUS (facoltativo)
- Ripeti con test_size = 0.1, 0.3, 0.5, 0.7. Come cambia l'accuratezza e la
  sua variabilita'? Che cosa succede se il training e' troppo piccolo?
- Disegna le 20 accuratezze come istogramma.
- Prova lo stesso esperimento con LogisticRegression(max_iter=200): e' piu' stabile
  dell'albero?

Scrivi il tuo codice qui sotto.
"""

