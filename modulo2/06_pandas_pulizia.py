"""Esercizio 6 (Modulo 2) - Pulire dati sporchi.

Teoria: teoria/03_numpy_pandas.md, sezione 7.

OBIETTIVO
Prendere una tabella con duplicati, valori mancanti e numeri scritti come
testo, e ripulirla passo per passo. E' il lavoro che occupa gran parte del
tempo in qualsiasi progetto di dati reali.

DATI DI PARTENZA (copiali nel tuo codice)
    dati = {
        "nome":  ["Anna", "Marco", "Luca", "Marco", "Sara", "Paolo"],
        "eta":   [23, 25, None, 25, "24", 27],
        "citta": ["Roma", "Milano", "Roma", "Milano", None, "Milano"],
        "voto":  [28, 24, 30, 24, 26, None],
    }
    df = pd.DataFrame(dati)

PROBLEMI PRESENTI
- la riga 3 (Marco) e' un duplicato della riga 1;
- "eta" contiene un valore mancante (None) e un numero scritto come TESTO ("24");
- "citta" ha un valore mancante;
- "voto" ha un valore mancante.

PASSI
1. Ispeziona: df.info() e df.isna().sum(). Annota cosa vedi: "eta" e'
   di tipo object (misto testo/numeri).
   Attesi i mancanti: eta 1, citta 1, voto 1.
2. Duplicati: stampa df.duplicated().sum() (-> 1), poi elimina con
   df = df.drop_duplicates(). Ora le righe sono 5 (ma gli indici 0,1,2,4,5:
   usa df = df.reset_index(drop=True) per rinumerarli).
3. Tipi: converti "eta" in numero:
       df["eta"] = pd.to_numeric(df["eta"], errors="coerce")
   Ora "eta" e' float, con il mancante come NaN.
4. Mancanti:
   - "eta": riempi con la MEDIANA (piu' robusta della media agli outlier):
         df["eta"] = df["eta"].fillna(df["eta"].median())
     La mediana di [23, 25, 24, 27] e' 24.5.
   - "citta": riempi con "sconosciuta".
   - "voto": riempi con la media dei voti presenti: (28+24+30+26)/4 = 27.0.
5. Controllo finale: df.isna().sum() deve essere tutto 0; df.info()
   senza object inattesi; df.describe() sensato.
6. Converti "eta" in intero (se non ci sono piu' NaN): df["eta"].astype(int)
   Attenzione: 24.5 diventa 24: e' una scelta, annotala in un commento.

RISULTATO ATTESO
    nome    eta  citta        voto
    Anna    23   Roma         28.0
    Marco   25   Milano       24.0
    Luca    24   Roma         30.0     (eta riempita: 24.5 -> 24 dopo astype)
    Sara    24   sconosciuta  26.0
    Paolo   27   Milano       27.0     (voto riempito)

CONCETTI NUOVI
- isna, sum per contare i mancanti; NaN (valore mancante dei decimali).
- duplicated, drop_duplicates, reset_index.
- pd.to_numeric con errors="coerce": cio' che non si converte diventa NaN.
- fillna con media, mediana o valore fisso; dropna.
- Scelte di pulizia: eliminare o riempire? Dipende da quanti mancanti ci
  sono e dal significato della colonna.

COME VERIFICARE DA SOLO
    assert len(df) == 5
    assert df.isna().sum().sum() == 0
    assert df.loc[df["nome"] == "Luca", "eta"].iloc[0] in (24, 24.5)
    assert df.loc[df["nome"] == "Paolo", "voto"].iloc[0] == 27.0
    assert df.loc[df["nome"] == "Sara", "citta"].iloc[0] == "sconosciuta"
    assert df["nome"].is_unique

ERRORI TIPICI
- Dimenticare di riassegnare: df.drop_duplicates() restituisce una nuova
  tabella, non modifica df. Serve df = df.drop_duplicates().
- Calcolare la mediana PRIMA della conversione in numero: non funziona su
  testo misto.
- Riempire con la media dopo aver gia' riempito altre colonne in modo che
  alteri i calcoli: segui l'ordine duplicati -> tipi -> mancanti.
- Eliminare tutte le righe con dropna() quando i mancanti sono tanti: si
  perdono quasi tutti i dati.

BONUS (facoltativo)
- Aggiungi una colonna "eta_era_mancante" (True/False) PRIMA del riempimento:
  tenere traccia di cio' che e' stato ricostruito e' una buona pratica.
- Prova dropna() invece di fillna e confronta quante righe restano.
- Scrivi una funzione pulisci(df) che esegue tutti i passi e la ripulisce
  qualunque tabella con quelle colonne.

Scrivi il tuo codice qui sotto.
"""

