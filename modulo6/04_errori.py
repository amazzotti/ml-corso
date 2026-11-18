"""Progetto (Modulo 6) - Passo 4: analisi degli errori.

Teoria: teoria/06_reti_neurali.md; teoria/05_ml_classico.md, sezioni 6 e 7.

OBIETTIVO
Guardare con i tuoi occhi le cifre che la rete sbaglia, capire se sono errori
"scusabili" (cifre ambigue) o sbagli veri, e studiare quanto la rete era sicura di se'.

PREPARAZIONE
Usa la rete e i pesi del passo 2 (modello.pt) e le previsioni del passo 3. Per le immagini da
disegnare servono quelle NON normalizzate oppure vanno "de-normalizzate":
       immagine_da_mostrare = immagine * 0.3081 + 0.1307
(inverso di Normalize).

PASSI
1. Individua gli indici degli errori:
       indici_errori = np.where(prev != vere)[0]       # tra 220 e 290 indici (272 nell'esecuzione di riferimento)
   Stampa quanti sono e le prime 10 coppie (vera, prevista).
2. Disegna una griglia 4 x 8 con 32 errori. Come titolo di ogni immagine: "vera -> prevista".
   Salva in modulo6/grafici/04_errori.png.
   Guarda attentamente. Per ciascuno chiediti: io l'avrei letta giusta? Molte sono scritte male
   o davvero ambigue (un "4" chiuso che sembra un "9"), alcune invece sembrano chiare:
   sono gli errori "veri" del modello.
3. FIDUCIA DELLA RETE. Per ogni campione calcola la probabilita' assegnata alla classe prevista:
       with torch.no_grad():
           probabilita = torch.softmax(rete(X), dim=1)
           fiducia, previsione = probabilita.max(dim=1)
   (Qui serve la softmax: CrossEntropyLoss la applicava da sola in addestramento; per avere
   le probabilita' la applichi tu.) Raccogli le fiducie di tutto il test set.
4. Confronta la fiducia media tra previsioni GIUSTE e previsioni SBAGLIATE.
   Attesi (esecuzione di riferimento): giuste 0.986; sbagliate 0.742.
   La rete e' in genere meno sicura quando sbaglia: la fiducia e' un'informazione utile.
5. Disegna due istogrammi sovrapposti della fiducia (giuste contro sbagliate, alpha = 0.5,
   scala logaritmica sull'asse y). Salva in modulo6/grafici/04_fiducia.png.
6. Errori "sicuri": trova quelli con fiducia > 0.95 (la rete era sicurissima e ha sbagliato).
   Quanti sono? (Riferimento: 49 su 272, cioe' circa un errore su sei.)
   Disegnali: e' probabile che siano etichette discutibili o cifre molto strane.
7. Politica di rifiuto: decidi una soglia (es. 0.9). Se la fiducia e' sotto soglia la rete
   "si astiene" (passa la cifra a una persona). Per soglie 0.5, 0.7, 0.9, 0.99 calcola:
       - la frazione di campioni su cui la rete risponde (copertura);
       - l'accuratezza SOLO sui campioni su cui risponde.
   Valori di riferimento (copertura / accuratezza sulle risposte date):
       soglia 0.5:  99,6% / 97,5%     soglia 0.7:  97,7% / 98,4%
       soglia 0.9:  94,1% / 99,3%     soglia 0.99: 83,5% / 99,8%
   Alzando la soglia l'accuratezza sale (fino al 99,8%) ma la copertura scende: con 0.99 la
   rete risponde solo a 5 cifre su 6, ma quasi non sbaglia.
   Scrivi in un commento un esempio di applicazione in cui preferiresti questo compromesso
   (es. smistamento postale: meglio far rileggere a una persona i casi incerti).
8. Scrivi 5-8 righe di analisi: tipi di errori, cifre piu' confuse, cosa potrebbe aiutare
   (piu' dati, piu' epoche, data augmentation, un'architettura convoluzionale).

CONCETTI NUOVI
- Analisi qualitativa degli errori: guardare i dati, non solo i numeri.
- Softmax per ottenere probabilita' (fiducia) dai logits.
- Calibrazione e fiducia: sbagliare con alta fiducia e' peggio.
- Copertura contro accuratezza: la politica di rifiuto.

COME VERIFICARE DA SOLO
    assert len(indici_errori) == (prev != vere).sum()
    assert fiducia_giuste.mean() > fiducia_sbagliate.mean()
    assert accuratezza_con_soglia_alta > 0.995                # soglia 0.99: circa 0.998
    assert copertura_soglia_alta < copertura_soglia_bassa

ERRORI TIPICI
- Dimenticare di de-normalizzare le immagini prima di disegnarle: il contrasto e' strano.
- Applicare softmax due volte o dimenticarla quando si vogliono le probabilita'.
- Confondere indici del test set con indici dei soli errori.
- Fare il calcolo della fiducia con la rete in modalita' train.
- Dimenticare torch.no_grad() (memoria in piu', nessun errore).

BONUS (facoltativo)
- Mostra, per qualche errore, le tre cifre piu' probabili con le loro probabilita'.
- Controlla se una cifra specifica (ad esempio il 5) ha piu' errori delle altre.
- Aggiungi rumore o ruota le immagini di 15 gradi e misura quanto cala l'accuratezza: la rete
  non e' robusta a cambiamenti che a un essere umano non darebbero fastidio.

Scrivi il tuo codice qui sotto.
"""

