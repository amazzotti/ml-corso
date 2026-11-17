"""Esercizio 7 (Modulo 4) - Un dataset reale e sporco: il Titanic.

Teoria: teoria/05_ml_classico.md, sezione 8.

OBIETTIVO
Addestrare un classificatore su dati reali con valori mancanti e colonne di testo,
usando una Pipeline che prepara i dati senza leakage.

IL DATASET
    from sklearn.datasets import fetch_openml
    df = fetch_openml("titanic", version=1, as_frame=True, parser="liac-arff").frame
(La prima volta serve connessione a Internet; poi viene salvato in locale.
Il parametro parser="liac-arff" evita un errore con versioni recenti di pandas.)
1309 passeggeri, 14 colonne. Usa solo queste:
    pclass    classe del biglietto (1, 2, 3)
    sex       "female" / "male"
    age       eta' (263 valori MANCANTI)
    fare      prezzo del biglietto (1 mancante)
    embarked  porto d'imbarco "C", "Q", "S" (2 mancanti)
    survived  ETICHETTA: 1 = sopravvissuto, 0 = no
Le altre colonne (name, ticket, cabin, boat, body, home.dest) le ignori: boat e body
"svelerebbero" la risposta (boat = su quale scialuppa e' salito!): usarle sarebbe
LEAKAGE.

PASSI
1. Preparazione iniziale:
       X = df[["pclass", "sex", "age", "fare", "embarked"]].copy()
       X["pclass"] = X["pclass"].astype(int)
       y = df["survived"].astype(int)        # e' testo '0'/'1' -> intero
2. Esplora: X.shape (1309, 5); X.isna().sum() (age 263, fare 1, embarked 2);
   y.value_counts():  0 -> 809,  1 -> 500.
   Domanda: qual e' l'accuratezza del modello "sempre non sopravvissuto"?
   809 / 1309 = 0.618. E' il riferimento da battere (DummyClassifier).
3. Dividi:  train_test_split(X, y, test_size=0.25, random_state=42, stratify=y).
4. Costruisci il preprocessing con ColumnTransformer:
   - colonne numeriche ["pclass", "age", "fare"]: SimpleImputer(strategy="median")
     poi StandardScaler;
   - colonne categoriche ["sex", "embarked"]: SimpleImputer(strategy="most_frequent")
     poi OneHotEncoder(handle_unknown="ignore").
   (Vedi lo schema completo nella teoria, sezione 8.)
5. Pipeline = preprocessing + modello. Addestra e valuta sul test (stesso split):
       Dummy             test 0.619
       LogisticRegression(max_iter=1000)   train 0.781   test 0.796
       DecisionTreeClassifier(max_depth=3, random_state=0)   train 0.803   test 0.838
       albero senza limite   train 0.966   test 0.765     <- overfitting
6. Estrai e leggi i coefficienti della regressione logistica con i nomi delle feature:
       nomi = modello["pre"].get_feature_names_out()
       coef = modello["clf"].coef_[0]
   Quale feature ha l'effetto piu' forte sulla sopravvivenza? ("sex_male" ha un peso
   fortemente NEGATIVO: essere uomo riduce molto la probabilita'; "pclass" negativo:
   piu' alta e' la classe numerica (3a), meno probabilita'.)
7. Scrivi 5 righe di commento: cosa hanno imparato i modelli? Corrisponde alla storia
   ("prima le donne e i bambini", e la prima classe piu' vicina alle scialuppe)?

CONCETTI NUOVI
- Valori mancanti: imputazione (mediana per i numeri, valore piu' frequente per le categorie).
- Variabili categoriche: one-hot encoding.
- Standardizzazione.
- ColumnTransformer + Pipeline: preparazione e modello in un oggetto unico, imparati solo
  sul training (nessun leakage).
- Leakage di colonne: alcune feature contengono (di fatto) la risposta.
- Modello di riferimento (Dummy).

COME VERIFICARE DA SOLO
    assert X.shape == (1309, 5)
    assert X.isna().sum().to_dict() == {"pclass": 0, "sex": 0, "age": 263, "fare": 1, "embarked": 2}
    assert y.value_counts().to_dict() == {0: 809, 1: 500}
    assert abs(dummy.score(X_test, y_test) - 0.619) < 0.003
    assert abs(logreg.score(X_test, y_test) - 0.796) < 0.01
    assert logreg.score(X_test, y_test) > dummy.score(X_test, y_test)

ERRORI TIPICI
- Imputare/scalare l'intero dataset PRIMA di dividere (leakage). Con la Pipeline non succede.
- Usare colonne come "boat" o "body": leakage grave, accuratezze irreali (> 95%).
- Passare a fit() una colonna con tipo "category" non convertito: se vedi errori sui
  tipi, converti con .astype(str) le colonne di testo prima dell'imputazione.
- Usare la LabelEncoder / numeri 0,1,2 per i porti: introduce un ordine inesistente.

BONUS (facoltativo)
- Aggiungi la feature "familiari" = sibsp + parch (dal dataframe originale) e vedi se
  migliora.
- Aggiungi un'indicatrice "eta_mancante" (True/False) prima dell'imputazione: a volte
  il fatto che manchi l'eta' porta informazione.
- Confronta mediana e media come strategia di imputazione.
- Prova RandomForestClassifier(n_estimators=200, random_state=0): test 0.799. Meglio o no?

Scrivi il tuo codice qui sotto.
"""

