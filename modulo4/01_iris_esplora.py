"""Esercizio 1 (Modulo 4) - Esplorare il dataset Iris.

Prima di iniziare:  pip install scikit-learn      (ambiente .venv attivo)
Teoria: teoria/05_ml_classico.md, sezione 1.

OBIETTIVO
Conoscere bene i dati PRIMA di usare qualsiasi modello: com'e' fatto il
dataset, che classi ci sono, quali caratteristiche le distinguono.

DATASET
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    X = iris.data         # tabella con 4 feature (cm)
    y = iris.target       # 0 = setosa, 1 = versicolor, 2 = virginica
    nomi = iris.target_names
150 fiori, 4 feature, 3 specie (50 ciascuna).

PASSI
1. Stampa X.shape  ->  (150, 4)   e le colonne:
       sepal length (cm), sepal width (cm), petal length (cm), petal width (cm)
2. Stampa le prime righe (head) e X.describe().
   Medie attese:  sepal length 5.843   sepal width 3.057
                  petal length 3.758   petal width 1.199
3. Quanti fiori per classe?  y.value_counts()  ->  50, 50, 50 (dataset bilanciato).
4. Media di ciascuna feature PER CLASSE:
       X.groupby(y).mean()
   Attese per "petal length (cm)":  setosa 1.462, versicolor 4.260, virginica 5.552.
   Quale feature separa meglio le tre specie? (Guarda la differenza tra le medie
   rispetto alla dispersione: i petali separano molto meglio dei sepali.)
5. Grafici (salva in modulo4/grafici/):
   a) scatter di "petal length" contro "petal width", colore = classe
      (ax.scatter(..., c=y)). Cosa osservi? La setosa e' ben separata dalle altre;
      versicolor e virginica si sovrappongono un po' al confine.
   b) lo stesso con "sepal length" contro "sepal width": le classi si mescolano di piu'.
   c) istogramma di "petal length" per ciascuna classe, sovrapposti con alpha=0.5.
6. Scrivi in un commento 3-4 righe: quali feature sembrano piu' utili, quali due
   classi saranno probabilmente le piu' difficili da distinguere, e perche'.

VOCABOLARIO IN PRATICA
- Campione: un fiore (una riga).   - Feature: le 4 misure.   - Etichetta: la specie.
- Classificazione MULTICLASSE (3 classi). Dataset BILANCIATO (stesso numero per classe).

COME VERIFICARE DA SOLO
    assert X.shape == (150, 4)
    assert y.value_counts().tolist() == [50, 50, 50]
    assert abs(X["petal length (cm)"].mean() - 3.758) < 0.001
    medie = X.groupby(y).mean()
    assert abs(medie.loc[0, "petal length (cm)"] - 1.462) < 0.001
    assert abs(medie.loc[2, "petal length (cm)"] - 5.552) < 0.001

ERRORI TIPICI
- Dimenticare as_frame=True: senza, X e' un array NumPy e head/describe/groupby non esistono.
- Confondere il numero della classe (0, 1, 2) con il nome (setosa, ...): usa
  nomi[classe] per tradurre.
- Concludere dai soli numeri senza guardare i grafici.

BONUS (facoltativo)
- Matrice di grafici a dispersione con pandas:
      from pandas.plotting import scatter_matrix
      scatter_matrix(X, c=y, figsize=(8, 8))
- Calcola la matrice di correlazione X.corr() e commenta la coppia piu'
  correlata ("petal length" e "petal width", circa 0.96).
- Prevedi "a occhio": con una regola semplice sulla sola "petal length"
  (es. < 2.5 -> setosa, < 4.9 -> versicolor, altrimenti virginica) quanti
  fiori classifichi bene? Scrivi la regola e calcola l'accuratezza con NumPy
  (con queste soglie: 0.953, cioe' 143 fiori su 150).
  Hai appena costruito a mano un piccolo albero decisionale.

Scrivi il tuo codice qui sotto.
"""

