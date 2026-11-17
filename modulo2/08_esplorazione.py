"""Esercizio 8 (Modulo 2) - Mini analisi completa di un dataset.

Teoria: tutto teoria/03_numpy_pandas.md.

OBIETTIVO
Mettere insieme quello che hai imparato: caricare un dataset reale,
esplorarlo, calcolare statistiche per gruppo e produrre grafici
commentati. Alla fine scrivi un breve riassunto delle scoperte.

DATASET: WINE (incluso in scikit-learn, nessun download)
Prima installa:  pip install scikit-learn
    from sklearn.datasets import load_wine
    dati = load_wine(as_frame=True)
    df = dati.frame                 # tabella con 13 caratteristiche + colonna "target"
    nomi_classi = dati.target_names # ['class_0', 'class_1', 'class_2']
Sono 178 campioni di vino di tre produttori (classi). Le caratteristiche
sono misure chimiche (alcol, acido malico, fenoli, colore, ...).

PARTE 1 - ESPLORAZIONE
1. df.shape                     -> (178, 14)
2. df.head(), df.info(), df.describe()
3. Ci sono valori mancanti?  df.isna().sum().sum()     -> 0
4. Quanti campioni per classe? df["target"].value_counts()
   Attesi: classe 1: 71, classe 0: 59, classe 2: 48.

PARTE 2 - DOMANDE
5. Tra le colonne "alcohol", "malic_acid", "color_intensity", "proline":
   media e deviazione standard di ciascuna.
6. Media di "alcohol" per classe (groupby("target")):
   Attese circa: classe 0: 13.74, classe 1: 12.28, classe 2: 13.15.
7. Quale classe ha la "proline" media piu' alta? (La classe 0, circa 1116.)
8. Matrice di correlazione: df.corr(). Individua la coppia di colonne
   (diverse) con la correlazione piu' alta in valore assoluto e scrivila in
   un commento. Suggerimento: costruisci la matrice, metti a NaN la
   diagonale e usa .abs().stack().idxmax(), oppure ordinala a mano.
   (Una coppia molto correlata e' "flavanoids" con "total_phenols".)

PARTE 3 - GRAFICI (salvali in modulo2/grafici/)
9.  Istogramma di "alcohol".
10. Grafico a barre della media di "alcohol" per classe.
11. Scatter di "alcohol" contro "color_intensity", con il colore dei
    punti dato dalla classe:  ax.scatter(x, y, c=df["target"])
    Le classi si separano? Scrivi in un commento cosa osservi.
12. Scatter "flavanoids" contro "total_phenols" (la coppia piu' correlata).

PARTE 4 - RIASSUNTO
In un commento (o in un file "modulo2/riassunto_wine.md") scrivi 5-8 righe:
- com'e' fatto il dataset;
- cosa distingue le tre classi;
- quali caratteristiche sembrano piu' utili per riconoscere la classe;
- una cosa che ti ha sorpreso.
Queste osservazioni ti serviranno quando farai davvero classificazione.

CONCETTI RIPASSATI
- DataFrame, info/describe, value_counts, groupby, corr.
- Grafici: istogramma, barre, scatter colorato.
- Ragionare sui dati prima di usare un modello.

COME VERIFICARE DA SOLO
    assert df.shape == (178, 14)
    assert df.isna().sum().sum() == 0
    assert df["target"].value_counts().to_dict() == {1: 71, 0: 59, 2: 48}
    assert abs(df.groupby("target")["alcohol"].mean()[0] - 13.74) < 0.01

ERRORI TIPICI
- Dimenticare pip install scikit-learn (ModuleNotFoundError: sklearn).
- Dimenticare che "target" e' una colonna: includerla nelle statistiche
  delle caratteristiche (media del target non ha senso).
- Tracciare uno scatter senza etichette sugli assi.
- Trarre conclusioni forti da una sola correlazione: verifica con un grafico.

BONUS (facoltativo)
- Ripeti l'analisi con un altro dataset di sklearn: load_breast_cancer(as_frame=True)
  o load_diabetes(as_frame=True).
- Disegna tutte le coppie di 4 caratteristiche con una griglia di scatter
  (subplots 4x4) o con pandas.plotting.scatter_matrix.
- Standardizza ogni caratteristica ((x - media) / std) e confronta le
  statistiche prima e dopo.

Scrivi il tuo codice qui sotto.
"""

