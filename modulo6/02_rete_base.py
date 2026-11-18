"""Progetto (Modulo 6) - Passo 2: la rete base e il suo addestramento.

Teoria: teoria/06_reti_neurali.md, sezioni 3, 6 e 9.

OBIETTIVO
Costruire una rete densa che riconosce le cifre, scrivere il ciclo di addestramento
con mini-batch e registrare le curve di perdita e accuratezza.

L'ARCHITETTURA
       784 ingressi (28*28 pixel appiattiti)  ->  128 neuroni nascosti (ReLU)  ->  10 uscite
       class Rete(nn.Module):
           def __init__(self):
               super().__init__()
               self.strato1 = nn.Linear(784, 128)
               self.strato2 = nn.Linear(128, 10)
           def forward(self, x):
               x = x.view(x.size(0), -1)         # (N, 1, 28, 28) -> (N, 784)
               x = torch.relu(self.strato1(x))
               return self.strato2(x)             # logits: punteggi grezzi, NIENTE softmax
(Oppure con nn.Sequential(nn.Flatten(), nn.Linear(784, 128), nn.ReLU(), nn.Linear(128, 10)).)
Parametri: 784*128 + 128 + 128*10 + 10 = 101.770. Verificalo con
sum(p.numel() for p in rete.parameters()).

PERDITA E OTTIMIZZATORE
       perdita_fn = nn.CrossEntropyLoss()      # multiclasse; vuole LOGITS e etichette intere
       ottimizzatore = torch.optim.Adam(rete.parameters(), lr=0.001)
Perche' non c'e' la softmax nella rete? CrossEntropyLoss la applica da se' (insieme al logaritmo,
in modo piu' stabile). Mettere una softmax prima sarebbe un errore (teoria, sezione 10).

IL CICLO (5 epoche)
       for epoca in range(5):
           rete.train()
           for X, y in dati_train:
               ottimizzatore.zero_grad()
               perdita = perdita_fn(rete(X), y)
               perdita.backward()
               ottimizzatore.step()
           # a fine epoca: perdita media di training e accuratezza sul test (vedi sotto)
Valutazione a fine epoca:
       rete.eval()
       corrette = 0
       with torch.no_grad():
           for X, y in dati_test:
               corrette += (rete(X).argmax(dim=1) == y).sum().item()
       accuratezza = corrette / len(test)

PASSI
1. Prima di addestrare, controlla le forme su un batch:
       X, y = next(iter(dati_train));   rete(X).shape -> torch.Size([64, 10])
   E la perdita iniziale: circa 2.3 (= ln 10: la rete risponde a caso, probabilita' 0.1 per classe).
   Ricordati: ln(10) = 2.302. Verificalo con math.log(10).
2. PROVA DI SANITA': prima di addestrare su tutto, fai sovra-adattare UN SOLO batch per 100 passi
   (stesso X, y ripetuti): la perdita deve scendere vicino a 0. Se non succede c'e' un errore
   nel codice (teoria, sezione 10). Poi procedi.
3. Addestra per 5 epoche con torch.manual_seed(0) all'inizio. Il risultato esatto cambia un
   po' da un'esecuzione all'altra (ordine dei batch, versione di PyTorch, PC): conta
   l'ORDINE DI GRANDEZZA. Esempio di un'esecuzione di riferimento:
       epoca 1:  perdita train 0.255   accuratezza test 0.958
       epoca 2:  perdita train 0.111   accuratezza test 0.970
       epoca 3:  perdita train 0.076   accuratezza test 0.975
       epoca 4:  perdita train 0.059   accuratezza test 0.972
       epoca 5:  perdita train 0.048   accuratezza test 0.978
   Variazione misurata a 5 epoche con 5 seed diversi: accuratezza di test tra 0.971 e 0.978,
   media 0.974, deviazione standard 0.0015. Quindi un tuo risultato tra 0.970 e 0.980 e' normale.
   Osserva: la perdita di training scende sempre; l'accuratezza di test sale e puo' oscillare
   un po' (epoca 4). Gia' alla prima epoca circa il 95-96% delle cifre e' riconosciuto.
4. Registra per ogni epoca perdita di training e accuratezza di test e disegna le due curve
   (due grafici affiancati). Salva in modulo6/grafici/02_curve.png.
5. Calcola anche l'accuratezza sul TRAINING set a fine addestramento (con rete.eval() e no_grad).
   E' circa 0.986: confrontala con quella di test (circa 0.973-0.978). Il divario, di poco
   piu' di un punto, e' il segno di un leggero overfitting (teoria 05, sezione 6). Scrivi in
   un commento quanto e' grande.
6. Salva i pesi per il passo successivo:
       torch.save(rete.state_dict(), Path(__file__).parent / "modello.pt")
   (il file .pt e' ignorato da git).

CONCETTI NUOVI
- nn.Module con __init__ e forward; appiattimento delle immagini.
- CrossEntropyLoss su logits (con etichette intere).
- Ciclo di addestramento a mini-batch + valutazione a fine epoca.
- rete.train() / rete.eval(), torch.no_grad(), argmax per la classe prevista.
- Perdita iniziale attesa = ln(numero di classi).
- Prova di sanita': sovra-adattare un batch.

COME VERIFICARE DA SOLO
    assert n_parametri == 101770
    assert abs(perdita_iniziale - 2.3) < 0.15
    assert acc_test[0] > 0.94 and acc_test[-1] > 0.968
    assert perdite_train[-1] < perdite_train[0]
    assert acc_train > acc_test              # leggero overfitting

ERRORI TIPICI
- Dimenticare zero_grad(): la perdita non scende o impazzisce.
- Mettere softmax alla fine della rete con CrossEntropyLoss.
- Dimenticare rete.eval() e torch.no_grad() in valutazione (con questa rete non cambia il
  risultato, ma con dropout si').
- Accumulare la perdita come tensore (perdita invece di perdita.item()): consuma memoria.
- Dimenticare di moltiplicare per la dimensione del batch quando si calcola la perdita media
  dell'epoca (l'ultimo batch puo' essere piu' piccolo).
- Passare a CrossEntropyLoss etichette di tipo float: servono interi (long).

BONUS (facoltativo)
- Calcola il tempo per epoca con time.perf_counter().
- Prova batch_size = 16, 64, 256 e confronta tempo e accuratezza.
- Prova lr = 0.0001 e lr = 0.01: come cambiano le curve?
- Stampa la perdita ogni 100 passi durante la prima epoca per vedere la discesa iniziale.

Scrivi il tuo codice qui sotto.
"""

