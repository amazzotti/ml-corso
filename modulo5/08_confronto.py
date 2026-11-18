"""Esercizio 8 (Modulo 5) - A mano contro PyTorch: stessa rete, stessi risultati?

Teoria: teoria/06_reti_neurali.md, sezioni 5, 6 e 9.

OBIETTIVO
Dimostrare che la tua backpropagation scritta a mano (esercizio 4) e PyTorch
fanno ESATTAMENTE la stessa cosa, partendo dagli stessi pesi, e poi studiare
l'effetto di ottimizzatore, learning rate ed epoche.

PARTE A - STESSI PESI, STESSA RETE
1. Parti dall'inizializzazione dell'esercizio 4 (seed 0):
       rng = np.random.default_rng(0)
       W1 = rng.normal(0, 1, (2, 4));  b1 = np.zeros(4)
       W2 = rng.normal(0, 1, (4, 1));  b2 = np.zeros(1)
2. Costruisci in PyTorch la stessa rete, con SIGMOIDE negli strati (non tanh!) e in float64:
       rete = nn.Sequential(nn.Linear(2, 4), nn.Sigmoid(), nn.Linear(4, 1), nn.Sigmoid()).double()
   e copia i pesi di NumPy dentro PyTorch. Attenzione: nn.Linear memorizza i pesi
   TRASPOSTI (forma (uscite, ingressi)):
       with torch.no_grad():
           rete[0].weight.copy_(torch.tensor(W1.T));  rete[0].bias.copy_(torch.tensor(b1))
           rete[2].weight.copy_(torch.tensor(W2.T));  rete[2].bias.copy_(torch.tensor(b2))
3. Addestra con la STESSA ricetta: perdita MSE (nn.MSELoss), ottimizzatore SGD con lr = 1.0,
   1000 epoche, tutti e 4 i campioni per passo.
4. Risultato atteso dopo 1000 epoche:
       perdita PyTorch = 0.0238    perdita NumPy (esercizio 4, epoca 1000) = 0.0238
   Le due perdite coincidono (differenza < 1e-6). La tua backpropagation a mano e' esatta.
5. Confronta anche i gradienti al passo 0: dW1 di NumPy contro rete[0].weight.grad.T.
   Devono coincidere (np.allclose).

PARTE B - OTTIMIZZATORI E LEARNING RATE
Rete PyTorch dell'esercizio 7 (Linear-Tanh-Linear-Sigmoid, perdita BCE), seed 0, 2000 epoche.
Confronta e registra la perdita finale e l'epoca in cui scende sotto 0.01:
       Adam,  lr = 0.05    -> sotto 0.01 all'epoca 74;   perdita finale 0.00005
       Adam,  lr = 0.001   -> MAI sotto 0.01 in 2000 epoche; perdita finale 0.079 (troppo lento)
       SGD,   lr = 0.05    -> MAI sotto 0.01 in 2000 epoche; perdita finale 0.080 (troppo lento)
       SGD,   lr = 1.0     -> sotto 0.01 all'epoca 234;  perdita finale 0.0006 (non diverge)
   Nota: con tutti e quattro le uscite arrotondate sono gia' corrette ([0, 1, 1, 0]) anche
   quando la perdita e' ancora 0.08: la perdita e' piu' esigente dell'accuratezza.
Disegna le quattro curve della perdita (scala logaritmica) in un grafico.
Scrivi in un commento: quale ottimizzatore e' piu' "facile" da usare senza regolazioni?
(Adam, con il suo lr di default 0.001 funziona quasi sempre almeno decentemente.)

PARTE C - VARIABILITA' (non fidarti di un solo esperimento)
Ripeti l'addestramento della parte B (Adam, lr = 0.05) con 10 seed. Conta quanti imparano XOR
(uscite arrotondate = [0, 1, 1, 0]) e riporta quanti NO. Atteso: 9 seed su 10 imparano
(solo il seed 1 resta bloccato). Una frase onesta sui risultati:
"con questa rete e questi iperparametri XOR viene appreso in 9 seed su 10".

PARTE D - RIEPILOGO (da scrivere in un file modulo5/riassunto.md, 8-10 righe)
Con parole tue: neurone, attivazione, strato, forward, perdita, backpropagation, ottimizzatore,
epoca. Quale parte del lavoro fa PyTorch al posto tuo? Cosa resta a carico tuo?
(Scelta di architettura, perdita, ottimizzatore, learning rate, dati e valutazione.)

CONCETTI NUOVI
- Verifica incrociata di due implementazioni (a mano e libreria).
- nn.Linear salva i pesi trasposti: weight ha forma (uscite, ingressi).
- Confronto di ottimizzatori e learning rate.
- Variabilita' tra esecuzioni: riportare risultati su piu' seed.

COME VERIFICARE DA SOLO
    assert abs(perdita_torch - perdita_numpy) < 1e-6          # parte A
    assert abs(perdita_torch - 0.0238) < 0.001
    assert np.allclose(dW1_numpy, rete[0].weight.grad.T.numpy(), atol=1e-9)
    assert numero_di_seed_riusciti == 9                       # parte C: tutti tranne il seed 1

ERRORI TIPICI
- Dimenticare .double(): float32 contro float64 da' differenze di 1e-7 che sembrano errori.
- Non trasporre i pesi nel copiarli (W1.T, non W1).
- Usare tanh in una rete e sigmoide nell'altra.
- Confrontare MSE con BCE: sono perdite diverse, non i loro valori.
- Concludere da un solo seed.

BONUS (facoltativo)
- Aggiungi momentum a SGD: torch.optim.SGD(..., momentum=0.9). Cambia qualcosa?
- Prova weight_decay=1e-4 in Adam.
- Misura il tempo di addestramento a mano contro PyTorch (su 4 campioni la versione a mano
  e' piu' veloce: PyTorch ha un costo fisso; su 60000 immagini sarebbe tutto il contrario).

Scrivi il tuo codice qui sotto.
"""

