"""Esercizio 3 (Modulo 4) - Il primo classificatore: regressione logistica.

Teoria: teoria/05_ml_classico.md, sezioni 3, 4 e 7.

OBIETTIVO
Addestrare un classificatore su Iris, farlo prevedere, leggere le probabilita'
e la matrice di confusione.

PASSI
Usa la divisione dell'esercizio 2 (test_size=0.3, random_state=42, stratify=y).
1. Crea e addestra il modello:
       from sklearn.linear_model import LogisticRegression
       modello = LogisticRegression(max_iter=200)
       modello.fit(X_train, y_train)
2. Accuratezza:
       train: modello.score(X_train, y_train)  ->  0.971
       test:  modello.score(X_test, y_test)    ->  0.933
3. Previsioni sulle prime due righe del test:
       modello.predict(X_test.iloc[:2])        ->  [2 1]
   Le classi vere sono [2, 1]: entrambe giuste.
4. Probabilita':
       modello.predict_proba(X_test.iloc[:2])
   Attese (circa):
       [[0.000, 0.032, 0.968],     -> 96.8% virginica
        [0.005, 0.764, 0.232]]     -> 76.4% versicolor (23.2% virginica!)
   Ogni riga somma 1. Il modello e' MOLTO sicuro sul primo fiore, piu'
   incerto sul secondo. La classe prevista e' quella con la probabilita' piu' alta.
5. Matrice di confusione:
       from sklearn.metrics import confusion_matrix
       confusion_matrix(y_test, modello.predict(X_test))
   Attesa:
       [[15  0  0]
        [ 0 14  1]
        [ 0  2 13]]
   Righe = classe VERA, colonne = classe PREVISTA. La diagonale e' cio' che e'
   giusto (15 + 14 + 13 = 42 su 45 = 0.933). Gli errori sono tutti tra
   versicolor e virginica (1 + 2 = 3), mai la setosa: coincide con quello che
   hai visto nei grafici dell'esercizio 1.
6. classification_report(y_test, y_pred): leggi precisione, recall e F1 per classe.
   (Capirai bene precisione e recall nell'esercizio 6.)
7. Guarda i pesi: modello.coef_ (3 righe, 4 colonne: un peso per classe e per
   feature) e modello.intercept_. Quali feature hanno i pesi piu' grandi in
   valore assoluto per la virginica? (Attesi circa: petal length 2.33, petal width
   1.81, sepal width -0.34, sepal length 0.12: contano soprattutto i petali.)

PARTE B - LA FORTUNA DELLA DIVISIONE
Rifai l'esperimento con una divisione DIVERSA:
    train_test_split(X, y, test_size=0.2, random_state=42)     (senza stratify)
L'accuratezza di test diventa 1.000 (30 fiori, tutti giusti). Stesso modello,
stessi dati, risultato diverso (0.933 contro 1.000) solo per la divisione.
Scrivi in un commento cosa ne deduci sulla fiducia da dare a un singolo numero.

CONCETTI NUOVI
- Interfaccia scikit-learn: fit, predict, predict_proba, score.
- Probabilita' in uscita: sigmoide / softmax (teoria sezione 4).
- Matrice di confusione: righe = classe vera, colonne = prevista.
- max_iter: numero massimo di iterazioni dell'ottimizzatore (il modello si
  addestra con un metodo simile al gradient descent del Modulo 3).

COME VERIFICARE DA SOLO
    assert abs(modello.score(X_test, y_test) - 0.933) < 0.002
    assert list(modello.predict(X_test.iloc[:2])) == [2, 1]
    assert abs(modello.predict_proba(X_test.iloc[:1]).sum() - 1) < 1e-9
    cm = confusion_matrix(y_test, modello.predict(X_test))
    assert cm.trace() == 42 and cm.sum() == 45

ERRORI TIPICI
- ConvergenceWarning: aumenta max_iter (200 basta qui; con altri dati serve di piu')
  o standardizza le feature.
- Passare a predict dati con un numero di colonne diverso da quello del fit.
- Leggere la matrice di confusione con righe e colonne invertite.
- Usare predict_proba e dimenticare che l'ordine delle colonne e' quello di
  modello.classes_.

BONUS (facoltativo)
- Addestra il modello con standardizzazione (StandardScaler dentro una Pipeline)
  e confronta pesi e accuratezza.
- Prova LogisticRegression(C=0.01) (regolarizzazione forte) e C=100: come
  cambiano le probabilita' e l'accuratezza?
- Disegna la matrice di confusione con ConfusionMatrixDisplay.from_predictions.
- Costruisci un fiore inventato, ad esempio [5.0, 3.0, 4.0, 1.3], e osserva
  cosa prevede il modello e con che probabilita'.

Scrivi il tuo codice qui sotto.
"""

