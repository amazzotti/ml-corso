"""Esercizio 5 (Modulo 2) - Filtri, ordinamenti e raggruppamenti.

Teoria: teoria/03_numpy_pandas.md, sezione 6.
Usa il file "studenti.csv" creato nell'esercizio 4 (stesso contenuto).

OBIETTIVO
Rispondere a domande sui dati filtrando righe, ordinando e raggruppando.

DOMANDE (con il risultato atteso)
1. Studenti con voto >= 27.
       df[df["voto"] >= 27]
   Attese 4 righe: Anna (28), Luca (30), Giulia (29), Davide (27).
2. Studenti di Roma con voto >= 28 (due condizioni).
       df[(df["citta"] == "Roma") & (df["voto"] >= 28)]
   Attese 2 righe: Anna e Luca. Le parentesi attorno a ogni condizione
   sono obbligatorie; e' & e non "and".
3. Studenti di Roma OPPURE di Torino:  isin(["Roma", "Torino"]).   -> 5 righe
4. I 3 migliori voti, in ordine decrescente, con nome e voto.
       df.sort_values("voto", ascending=False).head(3)
   Attesi: Luca 30, Giulia 29, Anna 28.
5. Voto medio per citta':
       df.groupby("citta")["voto"].mean()
   Attesi: Milano 24.33, Roma 27.67, Torino 27.5.
6. Per ogni citta': media, massimo e numero di studenti, in un'unica tabella:
       df.groupby("citta")["voto"].agg(["mean", "max", "count"])
   Attesi: Milano (24.33, 27, 3), Roma (27.67, 30, 3), Torino (27.5, 29, 2).
7. Nuova colonna "fascia" con valori "alta" (voto >= 27) e "media" (altrimenti)
   usando np.where:
       df["fascia"] = np.where(df["voto"] >= 27, "alta", "media")
   Poi conta quanti studenti per fascia:  df["fascia"].value_counts()
   Attesi: alta 4, media 4.
8. L'eta' media degli studenti con fascia "alta" e di quelli con fascia "media".
   Attese: alta 24.0 (cioe' (23+22+23+28)/4), media 25.5 (cioe' (25+24+27+26)/4).
   Controllo: la media di 24.0 e 25.5 (stesso numero di studenti) e' 24.75,
   come l'eta' media generale.

CONCETTI NUOVI
- Filtro con maschera booleana: df[condizione].
- Condizioni combinate con & e | (e le parentesi); isin per piu' valori.
- sort_values, head.
- groupby: divide in gruppi, calcola per ciascuno, ricompone.
- agg con piu' funzioni; value_counts.
- np.where(condizione, valore_se_vero, valore_se_falso).

COME VERIFICARE DA SOLO
    assert len(df[df["voto"] >= 27]) == 4
    assert len(df[(df["citta"] == "Roma") & (df["voto"] >= 28)]) == 2
    assert df.sort_values("voto", ascending=False).iloc[0]["nome"] == "Luca"
    medie = df.groupby("citta")["voto"].mean()
    assert abs(medie["Roma"] - 83 / 3) < 1e-9
    assert medie["Torino"] == 27.5
    assert df["fascia"].value_counts()["alta"] == 4

ERRORI TIPICI
- df[df["voto"] >= 27 and ...]: ValueError. Servono & e le parentesi.
- Dimenticare le parentesi: df[df["citta"] == "Roma" & df["voto"] >= 28]
  da' un errore criptico sui tipi.
- Confondere df[colonna] (colonna) con df[condizione] (righe filtrate).
- Aspettarsi che sort_values modifichi df: restituisce una copia ordinata.
  Per tenerla: df_ordinato = df.sort_values(...).

BONUS (facoltativo)
- Aggiungi una colonna "scarto" = voto - media generale e ordina per scarto.
- Trova la citta' con la media piu' alta:  medie.idxmax().
- Calcola la correlazione tra eta' e voto: df[["eta", "voto"]].corr()
  e commenta in una riga che cosa significa.

Scrivi il tuo codice qui sotto.
"""

