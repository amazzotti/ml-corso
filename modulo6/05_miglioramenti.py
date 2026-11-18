"""Progetto (Modulo 6) - Passo 5: provare a migliorare.

Teoria: teoria/06_reti_neurali.md, sezioni 6 e 8; teoria/05_ml_classico.md, sezione 6.

OBIETTIVO
Condurre piccoli esperimenti controllati (cambiare UNA cosa alla volta) per vedere cosa migliora
la rete e cosa no, e imparare a riportare i risultati in modo onesto.

REGOLA DEGLI ESPERIMENTI
- Cambia una sola cosa per volta, tieni tutto il resto uguale (stesso seed, stesso numero di epoche).
- Misura sempre su validazione/test e confronta con la rete base del passo 2.
- Se la differenza e' piccola (< 0.3 punti), potrebbe essere solo rumore: ripeti con piu' seed.
- ATTENZIONE: se scegli la configurazione migliore guardando il test, il test non e' piu'
  "mai visto". Per un progetto serio: dividi il training in train (54.000) e validazione (6.000)
  con torch.utils.data.random_split, scegli sulla validazione e valuta UNA volta sul test.

Scrivi una funzione che riceve un modello e iperparametri e restituisce la storia dell'addestramento:
       def addestra(modello, epoche=5, lr=0.001, seed=0): ... return storia_acc_test, storia_perdita

ESPERIMENTI (con 5 epoche, seed 0, Adam, batch 64)
A. Rete base (passo 2)                    784-128-10                    101.770 parametri
       risultato atteso: accuratezza test 0.971-0.978 all'epoca 5 (media su 5 seed: 0.974)
B. Piu' neuroni e uno strato in piu' con dropout
       nn.Sequential(nn.Flatten(), nn.Linear(784, 256), nn.ReLU(), nn.Dropout(0.2),
                     nn.Linear(256, 128), nn.ReLU(), nn.Dropout(0.2), nn.Linear(128, 10))
       235.146 parametri.  Risultato atteso: accuratezza test circa 0.977 a 5 epoche.
       SORPRESA: con piu' del doppio dei parametri il vantaggio e' minimo (0.977 contro 0.974,
       quasi dentro il rumore). Una rete piu' grande e con dropout converge piu' lentamente (il
       dropout "disturba" l'addestramento) e dopo 5 epoche non ha ancora raggiunto il suo
       potenziale. Scrivi cosa ne deduci (vedi anche C).
C. La stessa rete B con 15 epoche. Atteso: accuratezza test 0.981 (misurata).
       Con piu' epoche la rete piu' grande con dropout supera la rete base (0.974):
       la differenza e' di circa 0.7 punti, ben oltre la deviazione standard (0.0015).
       (Registra tempi e curve: disegna le tre storie sullo stesso grafico.)
D. Learning rate: base con lr = 0.0001 e con lr = 0.01 (5 epoche). Cosa succede?
       lr = 0.0001: accuratezza 0.954 (converge lentamente: dopo 5 epoche e' ancora indietro);
       lr = 0.001 (base): 0.973;
       lr = 0.01: 0.950 (troppo alto per Adam: curva instabile, risultato peggiore).
   Sia troppo basso sia troppo alto peggiorano: il valore standard 0.001 di Adam e' un buon
   punto di partenza.
E. Dimensione del batch: 16, 64, 256. Piu' piccolo = piu' passi per epoca (piu' lento ma spesso
   piu' preciso per epoca); piu' grande = veloce ma aggiornamenti meno frequenti.
F. Rete convoluzionale (facoltativa, la piu' interessante):
       nn.Sequential(
           nn.Conv2d(1, 32, 3), nn.ReLU(), nn.MaxPool2d(2),     # (32, 13, 13)
           nn.Conv2d(32, 64, 3), nn.ReLU(), nn.MaxPool2d(2),    # (64, 5, 5)
           nn.Flatten(),                                         # 64*5*5 = 1600
           nn.Linear(1600, 128), nn.ReLU(), nn.Linear(128, 10))
   Le convoluzioni guardano piccole finestre dell'immagine e riconoscono forme (bordi, curve)
   ovunque compaiano. Tipicamente arriva intorno al 99% di accuratezza, ben oltre la rete densa.
   (Non e' nel piano del corso: e' il passo naturale successivo.)

PASSI
1. Implementa addestra() e ripeti A. Controlla che coincida con il passo 2.
2. Fai gli esperimenti B, C, D, E (e F se vuoi).
3. Compila una tabella (DataFrame pandas) con: nome, parametri, epoche, perdita train finale,
   accuratezza test finale, tempo. Stampala ordinata per accuratezza. Salva in
   modulo6/risultati_esperimenti.csv (file generato).
4. Ripeti la rete base con 5 seed diversi e riporta media +- deviazione standard dell'accuratezza
   di test. Valori misurati per i seed 0-4: 0.9728, 0.9713, 0.9752, 0.9742, 0.9754, cioe'
   media 0.974 +- 0.0015. Conclusione: due configurazioni che differiscono meno della
   deviazione standard non sono davvero diverse.
5. Scrivi 8-10 righe di conclusioni: cosa ha migliorato davvero, cosa no, cosa ti ha sorpreso.

CONCETTI NUOVI
- Esperimenti controllati (una variabile alla volta).
- Dropout, capacita' del modello e tempo di convergenza.
- Rumore tra esecuzioni: ripetere con piu' seed e riportare la deviazione standard.
- Rischio di "adattarsi al test" scegliendo con il test; ruolo della validazione.
- Convoluzioni (cenni).

COME VERIFICARE DA SOLO
    assert 0.968 < acc_base[-1] < 0.982
    assert len(tabella) >= 4
    assert media_seed - 3 * std_seed < acc_base[-1] < media_seed + 3 * std_seed

ERRORI TIPICI
- Confrontare esperimenti con seed o epoche diversi senza accorgersene.
- Cambiare piu' cose insieme e non sapere quale ha funzionato.
- Dimenticare model.eval() in valutazione con dropout: accuratezza bassa e instabile.
- Dimenticare di ricreare il modello tra un esperimento e l'altro: si riparte da pesi gia' addestrati.
- Scegliere la configurazione sul test e riportarla come risultato finale.
- Trarre conclusioni da differenze di 0.1 punti.

BONUS (facoltativo)
- Data augmentation: piccole rotazioni/traslazioni casuali nel training
  (transforms.RandomAffine(degrees=10, translate=(0.1, 0.1))). Aiuta la generalizzazione?
- Early stopping: salva i pesi dell'epoca con la migliore validazione e ricaricali alla fine.
- Prova SGD con momentum invece di Adam.

Scrivi il tuo codice qui sotto.
"""

