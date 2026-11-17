"""Esercizio 4 (Modulo 2) - Caricare un CSV con pandas.

Teoria: teoria/03_numpy_pandas.md, sezione 6.

OBIETTIVO
Creare un file CSV, caricarlo in un DataFrame, ispezionarlo e calcolare
qualche statistica. Il CSV di questo esercizio servira' anche al 05.

PASSO 1 - CREARE IL FILE "studenti.csv"
Puoi scriverlo a mano da VS Code (nella cartella modulo2), oppure generarlo
da Python con to_csv. Contenuto (prima riga = intestazione):
    nome,eta,citta,voto
    Anna,23,Roma,28
    Marco,25,Milano,24
    Luca,22,Roma,30
    Sara,24,Torino,26
    Paolo,27,Milano,22
    Giulia,23,Torino,29
    Elena,26,Roma,25
    Davide,28,Milano,27
Per generarlo da Python:
    df = pd.DataFrame({...})
    df.to_csv(percorso, index=False)     # index=False: niente colonna dell'indice
Usa il percorso relativo alla cartella del file:
    from pathlib import Path
    percorso = Path(__file__).parent / "studenti.csv"

PASSO 2 - CARICARE E ISPEZIONARE
    df = pd.read_csv(percorso)
    df.head()   df.shape   df.info()   df.describe()   df.columns
Stampa ciascuno e leggi con attenzione l'output: capire come e' fatto un
dataset prima di usarlo e' sempre il primo passo.

PASSO 3 - DOMANDE DA RISOLVERE CON IL CODICE
1. Quante righe e quante colonne ha la tabella?               -> (8, 4)
2. Qual e' il voto medio?                                     -> 26.375
3. Qual e' l'eta' media?                                      -> 24.75
4. Qual e' il voto massimo e chi lo ha preso?                 -> 30, Luca
   (suggerimento: df["voto"].idxmax() restituisce l'indice della riga;
    poi usa df.loc[indice, "nome"].)
5. Quanti studenti ci sono per citta'?                        -> Roma 3, Milano 3, Torino 2
   (df["citta"].value_counts())
6. Seleziona solo le colonne nome e voto.                      (doppie parentesi)
7. Aggiungi la colonna "voto_su_10" = voto / 3 e stampa le prime 3 righe.

CONCETTI NUOVI
- CSV: testo con valori separati da virgola, prima riga = nomi delle colonne.
- pd.read_csv, df.to_csv.
- DataFrame (tabella) e Series (una colonna).
- head, shape, info, describe, columns.
- Selezione di colonne: df["voto"] (una colonna) e df[["nome", "voto"]] (piu').
- value_counts, idxmax, mean, max.
- Nuova colonna: df["nuova"] = espressione sulle colonne esistenti.

COME VERIFICARE DA SOLO
    assert df.shape == (8, 4)
    assert df["voto"].mean() == 26.375
    assert df["eta"].mean() == 24.75
    assert df.loc[df["voto"].idxmax(), "nome"] == "Luca"
    assert df["citta"].value_counts()["Roma"] == 3
    assert list(df.columns)[:2] == ["nome", "eta"]

ERRORI TIPICI
- FileNotFoundError: il CSV non e' nella cartella indicata. Usa Path(__file__).parent.
- Selezionare piu' colonne con una sola coppia di parentesi: df["nome", "voto"]
  da' KeyError. Servono le doppie: df[["nome", "voto"]].
- Scrivere il CSV con spazi dopo le virgole: i nomi delle colonne avrebbero
  spazi iniziali.
- Dimenticare index=False in to_csv: compare una colonna in piu' ("Unnamed: 0").

BONUS (facoltativo)
- Calcola la deviazione standard dei voti (df["voto"].std(): attenzione,
  pandas divide per n-1, NumPy per n: i valori differiscono leggermente).
- Salva la tabella con la colonna in piu' in "studenti_v2.csv".
- Prova pd.read_csv con il parametro usecols=["nome", "voto"].

Scrivi il tuo codice qui sotto.
"""

