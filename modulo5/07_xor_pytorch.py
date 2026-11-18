"""Esercizio 7 (Modulo 5) - XOR in PyTorch: nn.Module, perdita, ottimizzatore.

Teoria: teoria/06_reti_neurali.md, sezioni 6 e 9.

OBIETTIVO
Risolvere XOR con PyTorch costruendo la rete con nn.Sequential e scrivendo il
ciclo di addestramento standard in 5 righe. Fare in 10 righe quello che
nell'esercizio 4 richiedeva 30 e la backpropagation a mano.

DATI
       X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
       Y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

LA RETE
       torch.manual_seed(0)
       rete = nn.Sequential(
           nn.Linear(2, 4),     # ingresso -> 4 neuroni nascosti
           nn.Tanh(),           # attivazione
           nn.Linear(4, 1),     # 4 -> 1 uscita
           nn.Sigmoid(),        # probabilita' tra 0 e 1
       )
Parametri: 2*4 + 4 + 4*1 + 1 = 17. Verificalo:
       sum(p.numel() for p in rete.parameters())    ->  17

L'ADDESTRAMENTO (da imparare a memoria)
       ottimizzatore = torch.optim.Adam(rete.parameters(), lr=0.05)
       perdita_fn = nn.BCELoss()                  # cross-entropy binaria
       for epoca in range(2000):
           ottimizzatore.zero_grad()              # 1. azzera i gradienti
           uscita = rete(X)                       # 2. forward
           perdita = perdita_fn(uscita, Y)        # 3. perdita
           perdita.backward()                     # 4. backpropagation
           ottimizzatore.step()                   # 5. aggiorna i pesi

PASSI
1. Costruisci la rete, stampala (print(rete)) e verifica i 17 parametri.
2. Scrivi il ciclo. Registra perdita.item() a ogni epoca.
3. Risultati attesi con torch.manual_seed(0):
       perdita all'epoca 1: 0.700     epoca 100: 0.0049     epoca 500: 0.0005     epoca 2000: ~0.0000
       uscite finali (arrotondate): [0, 1, 1, 0]
   Verifica con:
       with torch.no_grad(): print(rete(X).round().squeeze())   ->  tensor([0., 1., 1., 0.])
4. ESPERIMENTO SUI SEED: ripeti l'intero addestramento (ricreando rete e ottimizzatore) con
   torch.manual_seed(s) per s da 0 a 4:
       seed 0: impara    seed 2: impara    seed 3: impara    seed 4: impara
       seed 1: NON impara!  Perdita bloccata a 0.3466; uscite [0, 0.5, 1, 0.5].
   La rete e' rimasta bloccata in un minimo locale / plateau: stesso codice, stessi dati, ma
   un'inizializzazione sfortunata (con 10 seed solo il seed 1 fallisce). Scrivi in un commento cosa deduci (le reti neurali
   dipendono dall'inizializzazione; per questo si ripete l'addestramento con seed diversi
   e si riporta la variabilita').
5. Per il seed 1 prova a rimediare. Risultati attesi:
       8 neuroni nascosti (invece di 4)          -> impara
       Adam con lr = 0.01 e 5000 epoche          -> impara
       piu' epoche con lo stesso lr = 0.05 (6000) -> NON impara: aspettare non basta
   Cosa ti dice? (Una rete bloccata in un plateau non ne esce da sola: serve cambiare
   qualcosa, per esempio piu' capacita' o un diverso learning rate.)
6. Disegna in due grafici affiancati la curva della perdita (scala logaritmica) per il seed 0 e
   il seed 1. Salva in modulo5/grafici/07_xor_pytorch.png.
7. Disegna il confine di decisione sulla griglia [0,1] x [0,1] (come nell'esercizio 4).

CONFRONTO CON L'ESERCIZIO 4
- Quante righe di codice servivano per il backward a mano? Quante servono qui? (Zero.)
- Cosa e' cambiato? Il LAVORO e' lo stesso (forward, perdita, gradienti, aggiornamento),
  ma e' PyTorch a calcolare i gradienti.
- Cosa e' rimasto identico? Il ciclo, le epoche, il ruolo dello strato nascosto, la
  sensibilita' all'inizializzazione.

CONCETTI NUOVI
- nn.Sequential, nn.Linear, nn.Tanh, nn.Sigmoid.
- Perdita BCELoss (cross-entropy binaria) e ottimizzatore Adam.
- Ciclo di addestramento in 5 righe: zero_grad, forward, loss, backward, step.
- rete.parameters(), numero di parametri.
- Dipendenza dall'inizializzazione (seed).

COME VERIFICARE DA SOLO
    assert n_parametri == 17
    assert storia[0] > 0.6 and storia[-1] < 0.001            # seed 0
    assert rete(X).round().squeeze().tolist() == [0., 1., 1., 0.]
    # seed 1: esperimento, resta bloccato
    assert 0.34 < storia_seed1[-1] < 0.35

ERRORI TIPICI
- Dimenticare optimizer.zero_grad(): i gradienti si accumulano.
- Passare a BCELoss etichette di forma (4,) invece di (4, 1): errore o risultati sbagliati.
- Usare Y come interi (long): BCELoss richiede float.
- Dimenticare di ricreare la rete tra un seed e l'altro: si riparte dai pesi gia' addestrati.
- Aspettarsi risultati identici su un altro PC: i numeri esatti possono variare di poco
  con versioni diverse di PyTorch, ma il comportamento qualitativo resta.

BONUS (facoltativo)
- Sostituisci Adam con SGD (lr = 1.0 o 0.5): quante epoche servono?
- Sostituisci Tanh con ReLU: cambia il numero di seed che imparano?
- Allena la rete su altre funzioni logiche a 3 ingressi (parita' di 3 bit).
- Scrivi la rete come classe che estende nn.Module (con __init__ e forward) invece di
  nn.Sequential (teoria, sezione 9).

Scrivi il tuo codice qui sotto.
"""

